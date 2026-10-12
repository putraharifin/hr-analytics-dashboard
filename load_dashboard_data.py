import re
import pandas as pd
from sqlalchemy import create_engine

# Koneksi ke PostgreSQL lokal
DATABASE_URL = (
    "postgresql+psycopg2://hr_user:hr_local_password"
    "@localhost:5432/hr_analytics"
)

# Membaca CSV hasil notebook
df = pd.read_csv("employee_dashboard.csv")

# Mengubah nama kolom menjadi lowercase snake_case
def normalize_column(name):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"[^a-zA-Z0-9]+", "_", name)
    return name.strip("_").lower()

df.columns = [normalize_column(col) for col in df.columns]

# Memastikan kolom penting tersedia
required_columns = [
    "attrition",
    "attrition_status",
    "attrition_known",
    "employee_left",
    "department",
    "job_role",
    "over_time",
    "job_satisfaction",
    "years_at_company",
]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    raise ValueError(f"Kolom penting tidak ditemukan: {missing}")

# Memasukkan data ke PostgreSQL
engine = create_engine(DATABASE_URL)

with engine.begin() as connection:
    df.to_sql(
        "employee_data",
        con=connection,
        if_exists="replace",
        index=False,
        chunksize=500,
        method="multi"
    )

# Memeriksa hasil impor
with engine.connect() as connection:
    result = pd.read_sql(
        "SELECT COUNT(*) AS total_rows FROM employee_data",
        connection
    )

print("Data berhasil dimasukkan ke PostgreSQL.")
print(result)
