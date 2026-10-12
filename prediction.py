import argparse
from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL_PATH = BASE_DIR / "model" / "attrition_model.joblib"


def load_model(model_path):
    """Memuat model dan daftar fitur yang dibutuhkan."""
    artifact = joblib.load(model_path)

    if not isinstance(artifact, dict):
        raise ValueError("Format file model tidak sesuai.")

    if "model" not in artifact or "features" not in artifact:
        raise ValueError(
            "File model harus memiliki key 'model' dan 'features'."
        )

    return artifact["model"], artifact["features"], artifact.get(
        "model_name", "Unknown Model"
    )


def predict_attrition(input_path, model_path=DEFAULT_MODEL_PATH):
    """Memprediksi attrition dari file CSV berisi data karyawan."""

    # Memuat model
    model, required_features, model_name = load_model(model_path)

    # Membaca data input
    input_path = Path(input_path)
    data = pd.read_csv(input_path)

    if data.empty:
        raise ValueError("File input tidak memiliki baris data.")

    # Memeriksa fitur wajib
    missing_features = [
        feature
        for feature in required_features
        if feature not in data.columns
    ]

    if missing_features:
        raise ValueError(
            "Kolom berikut belum tersedia pada file input: "
            + ", ".join(missing_features)
        )

    # Menggunakan fitur sesuai urutan ketika training
    X_input = data[required_features].copy()

    # Prediksi kelas
    predictions = model.predict(X_input)

    # Menambahkan hasil prediksi
    results = data.copy()
    results["Predicted_Attrition"] = predictions
    results["Prediction_Label"] = results[
        "Predicted_Attrition"
    ].map({
        0: "Tidak Keluar",
        1: "Berpotensi Keluar"
    })

    # Menambahkan probabilitas jika model mendukungnya
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_input)
        classes = list(model.classes_)

        if 1 in classes:
            positive_index = classes.index(1)
            results["Attrition_Probability"] = (
                probabilities[:, positive_index] * 100
            ).round(2)

    # Menyimpan hasil di samping file input
    output_path = input_path.with_name(
        f"{input_path.stem}_prediction.csv"
    )
    results.to_csv(output_path, index=False)

    print(f"Model: {model_name}")
    print(f"Jumlah data diprediksi: {len(results)}")
    print("\nHasil prediksi:")
    columns_to_show = [
        "Predicted_Attrition",
        "Prediction_Label"
    ]

    if "Attrition_Probability" in results.columns:
        columns_to_show.append("Attrition_Probability")

    print(results[columns_to_show].to_string(index=False))
    print(f"\nHasil lengkap disimpan ke: {output_path}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Prediksi attrition karyawan Jaya Jaya Maju."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path ke file CSV berisi data karyawan."
    )

    parser.add_argument(
        "--model",
        default=str(DEFAULT_MODEL_PATH),
        help="Path ke file model .joblib."
    )

    args = parser.parse_args()

    predict_attrition(
        input_path=args.input,
        model_path=args.model
    )


if __name__ == "__main__":
    main()
