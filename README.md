## Business Dashboard

Dashboard HR Jaya Jaya Maju dikembangkan menggunakan Metabase untuk membantu departemen Human Resources memantau attrition karyawan dan mengeksplorasi faktor-faktor yang berkaitan dengan keluarnya karyawan.

Dashboard mencakup:
- KPI jumlah karyawan dengan label attrition valid, jumlah karyawan keluar, dan attrition rate.
- Perbandingan attrition berdasarkan departemen dan jabatan.
- Analisis attrition berdasarkan status lembur, kepuasan kerja, dan masa kerja.
- Visualisasi untuk mendukung identifikasi kelompok karyawan yang perlu ditinjau lebih lanjut.

**Catatan kualitas data:** terdapat 412 baris dengan label `Attrition` kosong. Perhitungan attrition rate hanya menggunakan baris dengan label valid. Oleh karena itu, hasilnya harus ditafsirkan sebagai attrition rate pada data berlabel, bukan estimasi pasti untuk seluruh populasi karyawan.

### Akses Dashboard

- Platform: Metabase lokal
- URL lokal: `http://localhost:3000`
- Username: putraharifin@gmail.com
- Password: putraharifin123
- Screenshot: `putraharifin25_dicoding-dashboard.png`
- Database Metabase: `metabase.db.mv.db`

Dashboard dapat dijalankan secara lokal setelah reviewer menyiapkan Docker, mengimpor database sumber data, dan memulihkan konfigurasi Metabase sesuai petunjuk proyek.