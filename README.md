# ☕ Coffee Sales A/B Testing – Diskon vs Tanpa Diskon

## 📌 Proyek Singkat
Proyek ini bertujuan untuk menguji efektivitas pemberian diskon terhadap peningkatan pembelian biji kopi. Melalui pendekatan **A/B Testing**, kami membandingkan total penjualan dari dua kelompok pelanggan: yang menerima diskon 20% dan yang tidak menerima diskon.

---

## 🎯 Tujuan

- Mengidentifikasi apakah pemberian diskon berpengaruh signifikan terhadap jumlah pembelian.
- Menganalisis perbedaan rata-rata penjualan antara dua kelompok.
- Memberikan rekomendasi strategis untuk keputusan bisnis terkait promosi dan diskon.

---

## 🗂️ Dataset

Dataset terdiri dari transaksi penjualan biji kopi dengan detail berikut:

| Kolom | Deskripsi |
|-------|-----------|
| `Date` | Tanggal pembelian |
| `Customer_ID` | ID pelanggan unik |
| `Category` | Kategori produk (Coffee Beans) |
| `Product` | Jenis kopi (Brazilian, Ethiopian, dsb.) |
| `Unit Price` | Harga per unit |
| `Quantity` | Jumlah unit yang dibeli |
| `Sales Amount` | Total penjualan sebelum diskon |
| `Used_Discount` | Apakah diskon digunakan (True/False) |
| `Discount_Amount` | Besar diskon (misal 20%) |
| `Final Sales` | Total penjualan setelah diskon |

---

## 🔍 Metodologi

1. **Data Cleaning & Preprocessing**
   - Pengecekan missing values
   - Pemeriksaan tipe data
2. **Exploratory Data Analysis (EDA)**
   - Visualisasi sebaran data
   - Perbandingan penjualan sebelum dan sesudah diskon
3. **A/B Testing**
   - Uji hipotesis (Independent T-Test)
   - Perbandingan rata-rata `Final Sales` antar kelompok
4. **Kesimpulan & Rekomendasi**
   - Apakah diskon berhasil meningkatkan pendapatan?

---


## 📈 Hasil Utama

- Terdapat perbedaan rata-rata penjualan antara grup diskon dan non-diskon.
- Hasil uji statistik menunjukkan bahwa [**hasil uji t-test** dimasukkan di sini jika signifikan/tidak].
- [Masukkan ringkasan insight utama, misal: "Diskon menaikkan volume pembelian, tapi menurunkan total revenue."]

---

## ✅ Kesimpulan

Pemberian diskon **[efektif/tidak efektif]** dalam meningkatkan total pembelian. Untuk strategi promosi berikutnya, disarankan untuk mempertimbangkan margin keuntungan per produk dan respon pelanggan terhadap diskon.

---

## 🚀 Jalankan Proyek
🔗 [Streamlit App](https://abtesting-mfxedswzedcic7xrjdgrgb.streamlit.app/)
