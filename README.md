# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan perusahaan yang menghadapi permasalahan terkait tingginya tingkat *attrition* atau karyawan yang meninggalkan perusahaan. Tingginya attrition dapat mengganggu operasional, meningkatkan biaya rekrutmen dan pelatihan, serta menyebabkan hilangnya pengalaman dan pengetahuan karyawan.

Oleh karena itu, proyek ini dilakukan untuk menganalisis karakteristik karyawan yang berkaitan dengan attrition, menyajikan hasil analisis melalui business dashboard, serta membangun prototype machine learning yang dapat membantu perusahaan mengidentifikasi karyawan yang berpotensi meninggalkan perusahaan.

### Permasalahan Bisnis

Permasalahan bisnis yang akan diselesaikan dalam proyek ini adalah:

1. Bagaimana tingkat attrition karyawan di Jaya Jaya Maju berdasarkan data yang tersedia?
2. Departemen dan posisi pekerjaan apa yang memiliki tingkat attrition relatif tinggi?
3. Apakah status lembur (*OverTime*), kepuasan kerja, dan masa kerja menunjukkan pola yang berbeda antara karyawan yang keluar dan yang tetap bekerja?
4. Bagaimana menyajikan informasi attrition agar mudah dipahami oleh pihak manajemen melalui business dashboard?
5. Bagaimana membangun model machine learning yang dapat membantu mengidentifikasi karyawan yang berpotensi meninggalkan perusahaan?

### Cakupan Proyek

Cakupan proyek yang dikerjakan meliputi:

1. **Data Understanding:** memahami struktur dataset, tipe data, distribusi target, dan nilai yang hilang.
2. **Data Preparation:** memeriksa duplikasi, menangani data dengan target attrition yang tidak tersedia, serta mempersiapkan fitur untuk analisis dan pemodelan.
3. **Exploratory Data Analysis (EDA):** menganalisis hubungan antara attrition dan karakteristik karyawan, seperti departemen, posisi pekerjaan, lembur, kepuasan kerja, serta masa kerja.
4. **Business Dashboard:** membangun dashboard menggunakan Metabase untuk menyajikan indikator attrition dan faktor-faktor yang perlu ditinjau lebih lanjut.
5. **Machine Learning:** membandingkan model baseline, Logistic Regression, dan Random Forest untuk klasifikasi attrition.
6. **Prototype Prediction:** menyimpan model terpilih dan menyediakan script untuk melakukan prediksi terhadap data karyawan baru.
7. **Evaluation:** mengevaluasi model menggunakan Accuracy, Precision, Recall, F1-score, dan ROC-AUC apabila metrik tersebut dapat dihitung.

Hasil analisis dan prediksi digunakan sebagai alat bantu pengambilan keputusan, bukan sebagai dasar tunggal untuk menentukan nasib seorang karyawan.

### Persiapan

**Sumber data:** `employee_data.csv`, yaitu dataset karyawan yang disediakan untuk pengerjaan proyek Dicoding.

**Tools yang digunakan:**
- Python untuk pengolahan data dan pemodelan machine learning.
- Pandas dan NumPy untuk manipulasi data.
- Scikit-learn untuk preprocessing, pelatihan, dan evaluasi model.
- Matplotlib dan Seaborn untuk visualisasi data.
- Joblib untuk menyimpan dan memuat model machine learning.
- PostgreSQL untuk menyimpan data dashboard.
- Metabase untuk membangun business dashboard.
- Docker untuk menjalankan PostgreSQL dan Metabase.

**Setup environment:**

1. Pastikan Python dan pip sudah terpasang.
2. Clone atau unduh repository proyek.
3. Masuk ke direktori proyek.
4. Buat virtual environment dan aktifkan environment tersebut.

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

5. Instal seluruh dependensi:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

6. Pastikan file dataset tersedia di lokasi yang digunakan notebook atau script.
7. Jalankan notebook untuk melakukan analisis data dan pelatihan model.
8. Pastikan model hasil pelatihan tersimpan di `model/attrition_model.joblib` sebelum menjalankan prototype prediksi.
9. Untuk dashboard, jalankan layanan PostgreSQL dan Metabase menggunakan Docker Compose, lalu masukkan data dashboard ke PostgreSQL dan hubungkan database tersebut ke Metabase.

## Business Dashboard

Business dashboard dibuat menggunakan Metabase untuk membantu manajemen memantau attrition karyawan dan mengeksplorasi karakteristik yang berkaitan dengan karyawan yang meninggalkan perusahaan.

Dashboard menyajikan indikator dan visualisasi berikut:

1. Jumlah karyawan dengan label attrition yang tersedia.
2. Jumlah karyawan yang tercatat keluar.
3. Persentase attrition (*attrition rate*) berdasarkan karyawan yang memiliki label.
4. Perbandingan attrition berdasarkan departemen.
5. Perbandingan attrition berdasarkan status lembur (*OverTime*).
6. Perbandingan attrition berdasarkan posisi pekerjaan (*JobRole*).
7. Perbandingan attrition berdasarkan kepuasan kerja (*JobSatisfaction*).
8. Perbandingan attrition berdasarkan kelompok masa kerja.

Data dengan label attrition yang tidak tersedia tidak dimasukkan ke dalam perhitungan tingkat attrition. Dengan demikian, indikator dashboard dihitung berdasarkan data yang memiliki label target valid.

Dashboard dijalankan secara lokal menggunakan Metabase melalui alamat:

`http://localhost:3000`

**Link dashboard:** belum tersedia untuk akses publik karena dashboard dijalankan secara lokal.

Screenshot dashboard dapat ditambahkan pada repository dengan nama file, misalnya `username_dicoding-dashboard.png`.

## Menjalankan Sistem Machine Learning

Prototype machine learning digunakan untuk memprediksi apakah seorang karyawan berpotensi meninggalkan perusahaan berdasarkan karakteristik yang tersedia pada dataset.

Model yang dibandingkan meliputi Dummy Classifier sebagai baseline, Logistic Regression, dan Random Forest. Model yang digunakan oleh prototype adalah model yang disimpan selama proses pelatihan pada file `model/attrition_model.joblib`.

### Langkah menjalankan prototype

1. Pastikan virtual environment sudah aktif dan seluruh dependensi terpasang.
2. Pastikan file model `model/attrition_model.joblib` sudah tersedia.
3. Siapkan file CSV berisi data karyawan yang ingin diprediksi. Kolom input harus sesuai dengan fitur yang digunakan pada saat pelatihan, tanpa kolom target `Attrition` dan tanpa kolom identitas yang tidak digunakan oleh model.
4. Jalankan script prediksi melalui terminal:

```bash
python prediction.py --input sample_employee.csv
```

5. Script akan membaca data input, menjalankan prediksi, dan menyimpan hasilnya ke file CSV baru dengan akhiran `_prediction.csv`.

Hasil prediksi mencakup label prediksi attrition. Jika model mendukung `predict_proba`, hasil juga menyertakan estimasi probabilitas prediksi.

Label prediksi merupakan indikasi berdasarkan pola yang dipelajari model, bukan kepastian bahwa karyawan akan meninggalkan perusahaan.

**Link prototype:** belum tersedia untuk akses publik. Prototype dijalankan secara lokal melalui script Python.

## Conclusion

Proyek ini menghasilkan analisis data attrition karyawan, business dashboard untuk membantu manajemen mengeksplorasi pola attrition, serta prototype machine learning untuk mendukung identifikasi karyawan yang berpotensi meninggalkan perusahaan.

Dashboard membantu manajemen melihat perbedaan tingkat attrition berdasarkan departemen, posisi pekerjaan, lembur, kepuasan kerja, dan masa kerja. Sementara itu, model machine learning menyediakan pendekatan prediktif yang dapat digunakan sebagai informasi tambahan dalam proses pengambilan keputusan.

Hasil analisis perlu ditafsirkan secara hati-hati. Pola yang ditemukan tidak secara otomatis membuktikan hubungan sebab-akibat. Kinerja model juga perlu dinilai berdasarkan metrik evaluasi dan diuji kembali menggunakan data baru sebelum digunakan dalam operasional perusahaan.

### Rekomendasi Action Items

- **Evaluasi kondisi kerja:** tinjau beban kerja, kebijakan lembur, dan keseimbangan kehidupan kerja, khususnya pada kelompok yang menunjukkan tingkat attrition relatif tinggi.
- **Tinjau kepuasan karyawan:** lakukan survei dan diskusi dengan karyawan untuk memahami faktor yang memengaruhi kepuasan kerja, lingkungan kerja, dan hubungan dengan manajer.
- **Evaluasi retensi per departemen dan posisi:** identifikasi kelompok yang memiliki tingkat attrition tinggi, kemudian lakukan evaluasi berdasarkan kondisi dan kebutuhan masing-masing tim.
- **Perkuat program pengembangan karier:** evaluasi kesempatan promosi, pelatihan, dan pengembangan kompetensi karyawan.
- **Pantau indikator secara berkala:** perbarui dashboard secara rutin agar manajemen dapat memantau perubahan attrition dan mengevaluasi efektivitas program retensi.
- **Validasi model secara berkala:** evaluasi performa model menggunakan data terbaru, terutama Recall, Precision, F1-score, dan ROC-AUC. Gunakan prediksi sebagai alat bantu, bukan sebagai satu-satunya dasar keputusan terhadap karyawan.
