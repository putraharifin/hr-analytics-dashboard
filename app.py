from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Jaya Jaya Maju | HR Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 HR Analytics Dashboard")
st.caption("Jaya Jaya Maju — Employee Attrition Analysis")

DATA_PATH = Path(__file__).parent / "employee_dashboard.csv"


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


def to_binary(series):
    """Ubah label attrition menjadi 1 = keluar, 0 = bertahan."""
    mapping = {
        "yes": 1, "no": 0,
        "keluar": 1, "bertahan": 0,
        "resign": 1, "tidak resign": 0,
        "left": 1, "stayed": 0,
        "1": 1, "0": 0,
        "true": 1, "false": 0,
    }
    return series.astype("string").str.strip().str.lower().map(mapping)


if not DATA_PATH.exists():
    st.error(
        "File employee_dashboard.csv tidak ditemukan. "
        "Letakkan file tersebut satu folder dengan app.py."
    )
    st.stop()

df = load_data(DATA_PATH)

# Standarisasi label attrition tanpa menganggap label kosong sebagai 0.
if "EmployeeLeft" in df.columns:
    df["EmployeeLeft"] = pd.to_numeric(
        df["EmployeeLeft"], errors="coerce"
    )
    df.loc[~df["EmployeeLeft"].isin([0, 1]), "EmployeeLeft"] = float("nan")
else:
    source_col = "Attrition" if "Attrition" in df.columns else "AttritionStatus"
    if source_col in df.columns:
        df["EmployeeLeft"] = to_binary(df[source_col])
    else:
        df["EmployeeLeft"] = float("nan")

if "AttritionKnown" in df.columns:
    known_flag = pd.to_numeric(df["AttritionKnown"], errors="coerce")
    df["AttritionKnown"] = known_flag.eq(1) & df["EmployeeLeft"].notna()
else:
    df["AttritionKnown"] = df["EmployeeLeft"].notna()

# Pilihan filter
with st.sidebar:
    st.header("Filter Dashboard")
    st.caption("Filter diterapkan ke seluruh visualisasi.")

    if "Department" in df.columns:
        departments = sorted(df["Department"].dropna().astype(str).unique())
        selected_departments = st.multiselect(
            "Departemen",
            departments,
            default=departments,
        )
    else:
        selected_departments = None

    if "OverTime" in df.columns:
        overtime_options = sorted(df["OverTime"].dropna().astype(str).unique())
        selected_overtime = st.multiselect(
            "Status lembur",
            overtime_options,
            default=overtime_options,
        )
    else:
        selected_overtime = None

    cost_per_hire = st.number_input(
        "Estimasi biaya per rekrutmen ($)",
        min_value=0,
        value=3000,
        step=500,
        help="Asumsi untuk simulasi biaya, bukan biaya aktual perusahaan.",
    )

filtered = df.copy()

if selected_departments is not None:
    filtered = filtered[
        filtered["Department"].astype(str).isin(selected_departments)
    ]

if selected_overtime is not None:
    filtered = filtered[
        filtered["OverTime"].astype(str).isin(selected_overtime)
    ]

known = filtered[filtered["AttritionKnown"]].copy()
total_employees = len(filtered)
known_count = len(known)
left_count = int(known["EmployeeLeft"].eq(1).sum())
attrition_rate = (
    known["EmployeeLeft"].mean() * 100 if known_count else 0
)
overtime_count = (
    filtered["OverTime"].astype(str).str.lower().eq("yes").sum()
    if "OverTime" in filtered.columns else 0
)
estimated_cost = left_count * cost_per_hire

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Karyawan", f"{total_employees:,}")
c2.metric("Attrition Rate", f"{attrition_rate:.2f}%")
c3.metric("Karyawan Keluar", f"{left_count:,}")
c4.metric("Karyawan Lembur", f"{overtime_count:,}")

st.caption(
    f"Label attrition valid: {known_count:,} dari {total_employees:,} karyawan. "
    "Baris dengan label tidak diketahui tidak dihitung sebagai karyawan bertahan."
)

st.divider()


def attrition_by_group(data, group_col):
    """Ringkasan jumlah karyawan berlabel dan attrition rate per kategori."""
    valid = data[data["AttritionKnown"]].copy()
    if group_col not in valid.columns or valid.empty:
        return pd.DataFrame()

    result = (
        valid.groupby(group_col, dropna=False)
        .agg(
            Employees=("EmployeeLeft", "size"),
            AttritionRate=("EmployeeLeft", "mean"),
            EmployeesLeft=("EmployeeLeft", "sum"),
        )
        .reset_index()
    )
    result["AttritionRate"] *= 100
    result["EmployeesLeft"] = result["EmployeesLeft"].astype(int)
    return result.sort_values("AttritionRate", ascending=False)


left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Attrition berdasarkan Lembur")
    if "OverTime" in known.columns and not known.empty:
        overtime_summary = attrition_by_group(known, "OverTime")
        fig = px.bar(
            overtime_summary,
            x="OverTime",
            y="AttritionRate",
            text="AttritionRate",
            labels={
                "OverTime": "Status Lembur",
                "AttritionRate": "Attrition Rate (%)",
            },
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_layout(yaxis_ticksuffix="%", yaxis_range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Kolom OverTime belum tersedia atau tidak ada data berlabel.")

with right_chart:
    st.subheader("Attrition berdasarkan Masa Kerja")
    if "TenureGroup" in known.columns and not known.empty:
        tenure_summary = attrition_by_group(known, "TenureGroup")
        fig = px.bar(
            tenure_summary,
            x="TenureGroup",
            y="AttritionRate",
            text="AttritionRate",
            labels={
                "TenureGroup": "Kelompok Masa Kerja",
                "AttritionRate": "Attrition Rate (%)",
            },
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_layout(yaxis_ticksuffix="%", yaxis_range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Kolom TenureGroup belum tersedia.")

st.divider()

left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Attrition berdasarkan Jabatan")
    if "JobRole" in known.columns and not known.empty:
        role_summary = attrition_by_group(known, "JobRole")
        fig = px.bar(
            role_summary.sort_values("AttritionRate"),
            x="AttritionRate",
            y="JobRole",
            orientation="h",
            text="AttritionRate",
            hover_data=["Employees", "EmployeesLeft"],
            labels={
                "JobRole": "Jabatan",
                "AttritionRate": "Attrition Rate (%)",
                "Employees": "Karyawan berlabel",
                "EmployeesLeft": "Karyawan keluar",
            },
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_layout(xaxis_ticksuffix="%", xaxis_range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Kolom JobRole belum tersedia.")

with right_chart:
    st.subheader("Kepuasan Kerja vs Pendapatan")
    required = {"JobSatisfaction", "MonthlyIncome"}
    if required.issubset(known.columns) and not known.empty:
        scatter_data = known.copy()
        scatter_data["MonthlyIncome"] = pd.to_numeric(
            scatter_data["MonthlyIncome"], errors="coerce"
        )
        scatter_data["JobSatisfaction"] = pd.to_numeric(
            scatter_data["JobSatisfaction"], errors="coerce"
        )
        scatter_data = scatter_data.dropna(
            subset=["MonthlyIncome", "JobSatisfaction"]
        )
        if not scatter_data.empty:
            fig = px.scatter(
                scatter_data,
                x="MonthlyIncome",
                y="JobSatisfaction",
                color="EmployeeLeft",
                color_discrete_map={0: "#2E86AB", 1: "#E76F51"},
                opacity=0.65,
                labels={
                    "MonthlyIncome": "Pendapatan Bulanan",
                    "JobSatisfaction": "Kepuasan Kerja (1–4)",
                    "EmployeeLeft": "Keluar (1) / Bertahan (0)",
                },
                hover_data=[
                    c for c in ["JobRole", "OverTime", "YearsAtCompany"]
                    if c in scatter_data.columns
                ],
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Tidak ada data numerik yang valid untuk scatter plot.")
    else:
        st.info("Kolom JobSatisfaction atau MonthlyIncome belum tersedia.")

st.divider()

st.subheader("Ringkasan dan Estimasi Biaya")
m1, m2 = st.columns(2)
m1.metric("Estimasi Biaya Rekrutmen", f"${estimated_cost:,.0f}")
m2.caption(
    f"Simulasi: {left_count:,} karyawan keluar × "
    f"${cost_per_hire:,.0f} per rekrutmen. "
    "Angka ini adalah asumsi yang dapat diubah, bukan biaya aktual."
)

with st.expander("Lihat tabel ringkasan attrition"):
    group_options = [
        c for c in ["OverTime", "TenureGroup", "JobRole", "Department"]
        if c in known.columns
    ]
    if group_options and not known.empty:
        chosen_group = st.selectbox("Kelompok analisis", group_options)
        st.dataframe(
            attrition_by_group(known, chosen_group),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.warning("Kolom kategori atau data berlabel tidak tersedia.")

with st.expander("Lihat data yang sedang digunakan"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.caption(
    "Dashboard ini bersifat deskriptif. Hubungan antarvariabel tidak "
    "membuktikan sebab-akibat dan tidak menentukan secara pasti siapa yang resign."
)
