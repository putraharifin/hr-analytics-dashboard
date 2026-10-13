# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan perusahaan yang menghadapi permasalahan terkait tingginya tingkat _attrition_ atau karyawan yang meninggalkan perusahaan. Tingginya attrition dapat mengganggu operasional, meningkatkan biaya rekrutmen dan pelatihan, serta menyebabkan hilangnya pengalaman dan pengetahuan karyawan.

Oleh karena itu, proyek ini dilakukan untuk menganalisis karakteristik karyawan yang berkaitan dengan attrition, menyajikan hasil analisis melalui business dashboard, serta membangun prototype machine learning yang dapat membantu perusahaan mengidentifikasi karyawan yang berpotensi meninggalkan perusahaan.

### Permasalahan Bisnis

Jaya Jaya Maju menghadapi permasalahan tingginya tingkat karyawan yang meninggalkan perusahaan (_employee attrition_). Berdasarkan konteks studi kasus, tingkat attrition yang melebihi 10% menjadi perhatian bagi departemen Human Resources karena berpotensi meningkatkan biaya rekrutmen dan pelatihan, mengganggu kesinambungan operasional, serta menyebabkan hilangnya pengalaman dan kompetensi karyawan.

Perusahaan membutuhkan analisis berbasis data untuk memahami karakteristik karyawan yang berkaitan dengan attrition. Tanpa pemantauan yang sistematis, departemen HR berisiko terlambat mengidentifikasi kelompok karyawan yang membutuhkan perhatian dan kesulitan menentukan prioritas program retensi.

Oleh karena itu, proyek ini berfokus pada eksplorasi data karyawan, pembangunan business dashboard untuk memantau indikator attrition, serta pengembangan model machine learning sebagai alat bantu untuk mengidentifikasi pola risiko attrition.

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

**Sumber data:** IBM HR Analytics Employee Attrition & Performance — Kaggle.

**Link** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

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

---

## Business Dashboard

Business dashboard dibuat menggunakan Metabase untuk membantu manajemen memantau attrition karyawan dan mengeksplorasi karakteristik yang berkaitan dengan karyawan yang meninggalkan perusahaan.

### Panduan Kredensial Akses

Dashboard dijalankan secara lokal melalui Docker. Untuk memeriksa dan menguji dashboard ini, silakan gunakan kredensial non-pribadi berikut:

- **URL Akses Metabase:** `http://localhost:3000`
- **Email/Username:** `root@mail.com`
- **Password:** `root123`

### Komponen dan Visualisasi Dashboard
Dashboard dirancang dengan struktur yang bersih dan fokus penuh pada penyampaian intisari visual tanpa tumpukan teks interpretasi, menyajikan komponen-komponen berikut:
1. **KPI - Total Karyawan Berlabel:** Menampilkan jumlah total basis data karyawan yang memiliki label status valid (1.058 karyawan).
2. **KPI - Karyawan Keluar:** Menampilkan akumulasi jumlah karyawan yang terkonfirmasi keluar (179 karyawan).
3. **KPI - Attrition Rate Persen:** Menampilkan rasio persentase aktual perputaran karyawan (16.92%).
4. **Grafik Attrition Rate by Department:** Bar chart perbandingan tingkat perputaran karyawan antar-divisi operasional.
5. **Grafik Attrition Rate by Overtime:** Bar chart analisis pengaruh kebijakan lembur terhadap keputusan karyawan meninggalkan perusahaan.
6. **Grafik Attrition berdasarkan Job Role:** Horizontal bar chart yang memetakan persentase kerentanan attrition di setiap spesifikasi peran jabatan.
7. **Grafik Attrition berdasarkan Kepuasan Kerja:** Bar chart visualisasi korelasi linier antara tingkat kebahagiaan kerja (*Job Satisfaction*) dengan loyalitas staf.
8. **Grafik Attrition berdasarkan Years at Company:** Donut/Bar chart proporsi perputaran karyawan berdasarkan kelompok masa kerja (*Tenure Group*).

*Catatan Teknis Perhitungan:* Sebanyak 412 data dengan status *Attrition* kosong (NaN) telah difilter secara otomatis menggunakan kondisi `AttritionKnown = 1`. Langkah ini memastikan data kosong tersebut tidak dihitung salah sebagai karyawan yang bertahan, sehingga metrik *Attrition Rate* tetap akurat berada di angka **16.92%**.

---

## Menjalankan Sistem Machine Learning

Prototype machine learning digunakan untuk memprediksi apakah seorang karyawan berpotensi meninggalkan perusahaan berdasarkan karakteristik yang tersedia pada dataset.

Model yang dibandingkan meliputi Dummy Classifier sebagai baseline, Logistic Regression, dan Random Forest. Model yang digunakan oleh prototype adalah model yang disimpan selama proses pelatihan pada file

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

---

## Kesimpulan dan Analisis Mendalam (Business Insights)

Berdasarkan eksplorasi data (EDA) dan analisis multivariat, tingkat perputaran karyawan (_attrition rate_) Jaya Jaya Maju sebesar **16.92%** dipicu oleh akumulasi faktor kelelahan fisik (_burnout_), kerentanan adaptasi, serta struktur kompensasi pada level dasar. Berikut adalah interpretasi mendalam mengapa fenomena ini terjadi:

- **Mengapa Departemen Sales & Peran Sales Representative Paling Rentan (Attrition: 20.69% & 43.10%)?**
  Divisi Sales menghadapi tekanan target performa yang konstan, yang diperparah oleh tingginya mobilitas dinas (_Travel Frequently_ mencatatkan attrition **24.88%**). Kombinasi antara tekanan target lapangan, kelelahan fisik akibat perjalanan dinas, serta fakta bahwa kelompok ini didominasi oleh tingkat pendapatan level dasar membuat stabilitas mental kerja di peran ini menjadi yang paling rapuh di perusahaan.
- **Mengapa Karyawan Berstatus 'Single' Jauh Lebih Rentan (Attrition: 26.70%) Dibandingkan yang Menikah/Cerai?**
  Karyawan berstatus _single_ memiliki fleksibilitas hidup yang lebih tinggi dan tanggungan finansial keluarga yang lebih minim. Berdasarkan data, kelompok ini beririsan erat dengan kelompok usia muda (**18-25 tahun** dengan attrition **38.04%**) dan masa kerja awal (**0-1 tahun** dengan attrition **34.59%**). Mereka cenderung lebih berani mengambil risiko untuk pindah perusahaan apabila ekspektasi awal kerja tidak sesuai, merasa kurang mendapat bimbingan (_onboarding_), atau mendapatkan tawaran kompensasi yang sedikit lebih baik di luar.
- **Mengapa Kerja Lembur Berdampak Destruktif (Attrition: 31.92%)?**
  Analisis kombinasi membuktikan bahwa kebijakan lembur (_OverTime_) menjadi pemicu utama kerusakan loyalitas. Karyawan yang dipaksa lembur dengan kepuasan kerja rendah (_JobSatisfaction 1_) langsung melonjak angka attrition-nya hingga **40.00%**. Bahkan, lembur mampu mengikis kebahagiaan karyawan yang awalnya sangat puas (_JobSatisfaction 4_), di mana tingkat attrition mereka tetap menembus batas merah sebesar **22.00%**. Ini membuktikan adanya isu _burnout_ sistemik yang mendesak untuk dibenahi.
- **Mengapa Kepemilikan Saham (Stock Option) dan Kompensasi Menjadi Jangkar Retensi?**
  Karyawan dengan pendapatan di bawah **$3,000** memiliki attrition sebesar **28.67%**. Menariknya, stabilitas karyawan meningkat drastis ketika mereka diberikan fasilitas investasi jangka panjang. Karyawan tanpa opsi saham (_StockOptionLevel 0_) memiliki attrition **25.69%**, namun angka ini langsung terkunci aman di bawah **10%** ketika karyawan memiliki _Stock Option Level 1 & 2_. Hal ini menunjukkan bahwa keterikatan finansial jangka panjang (_financial golden handcuffs_) sangat efektif menahan laju mundurnya karyawan.

---

## Performa Model Machine Learning & Fitur Paling Berpengaruh

Untuk membantu HR mengidentifikasi risiko _attrition_ secara proaktif sebelum karyawan mengajukan pengunduran diri, telah dibangun model prediktif berbasis **Logistic Regression** dengan bobot kelas seimbang (_Balanced Class Weight_).

### 1. Evaluasi Performa Model (Pada Test Set)

- **ROC-AUC (0.8305):** Model memiliki kemampuan yang sangat kuat (83%) dalam membedakan karakteristik karyawan yang berisiko keluar dengan karyawan yang akan bertahan.
- **Recall (72.22%):** Model berhasil mendeteksi **26 dari 36 karyawan yang sesungguhnya keluar**. Dari perspektif bisnis HR, metrik ini adalah yang paling krusial karena meminimalkan risiko karyawan berpotensi keluar yang luput dari pantauan manajemen (_False Negatives_ hanya 10 orang).
- **Precision (36.11%):** Model menghasilkan _False Positives_ sebanyak 46 karyawan (diprediksi keluar, namun aslinya bertahan). Hal ini merupakan _trade-off_ kompromi bisnis yang dapat diterima oleh perusahaan, karena biaya untuk melakukan intervensi retensi jauh lebih murah dibandingkan biaya kehilangan karyawan kompeten secara mendadak.
- **Akurasi Keseluruhan:** **73.58%** pada data pengujian, membuktikan model stabil dan memiliki kemampuan generalisasi yang baik tanpa gejala _overfitting_.

### 2. Fitur Paling Berpengaruh (Feature Importance / Coefficients)

Berdasarkan koefisien model Logistic Regression, fitur-fitur yang memiliki bobot pengaruh paling besar dalam mendorong keputusan model memprediksi _Attrition = Yes_ adalah:

1. **OverTime (Lembur - Positif):** Menjadi prediktor positif terkuat. Adanya indikasi kerja lembur melipatgandakan peluang model untuk melabeli karyawan tersebut berisiko keluar.
2. **BusinessTravel (Sering Perjalanan Dinas - Positif):** Karyawan yang sering melakukan perjalanan bisnis dinilai oleh model memiliki kerentanan tinggi terhadap kejenuhan kerja.
3. **MonthlyIncome & StockOptionLevel (Kompensasi - Negatif):** Memiliki koefisien negatif terbesar. Semakin tinggi pendapatan bulanan dan level opsi saham yang dimiliki karyawan, secara drastis akan menurunkan probabilitas mereka diprediksi akan keluar.
4. **YearsAtCompany & YearsWithCurrManager (Masa Kerja & Relasi - Negatif):** Karyawan dengan masa kerja stabil dan memiliki kedekatan durasi dengan manajer saat ini secara otomatis dinilai oleh model sebagai kelompok karyawan yang aman dan loyal.

### Rekomendasi Action Items

- **Evaluasi kondisi kerja:** tinjau beban kerja, kebijakan lembur, dan keseimbangan kehidupan kerja, khususnya pada kelompok yang menunjukkan tingkat attrition relatif tinggi.
- **Tinjau kepuasan karyawan:** lakukan survei dan diskusi dengan karyawan untuk memahami faktor yang memengaruhi kepuasan kerja, lingkungan kerja, dan hubungan dengan manajer.
- **Evaluasi retensi per departemen dan posisi:** identifikasi kelompok yang memiliki tingkat attrition tinggi, kemudian lakukan evaluasi berdasarkan kondisi dan kebutuhan masing-masing tim.
- **Perkuat program pengembangan karier:** evaluasi kesempatan promosi, pelatihan, dan pengembangan kompetensi karyawan.
- **Pantau indikator secara berkala:** perbarui dashboard secara rutin agar manajemen dapat memantau perubahan attrition dan mengevaluasi efektivitas program retensi.
- **Validasi model secara berkala:** evaluasi performa model menggunakan data terbaru, terutama Recall, Precision, F1-score, dan ROC-AUC. Gunakan prediksi sebagai alat bantu, bukan sebagai satu-satunya dasar keputusan terhadap karyawan.
