# 📦 E-Commerce Data Analysis & Dashboard

Proyek ini merupakan analisis data menggunakan **E-Commerce Public Dataset (Olist)** untuk memahami pola penjualan produk, performa pengiriman, aktivitas seller, serta perilaku pelanggan.  
Hasil analisis disajikan dalam bentuk **Jupyter Notebook** dan **dashboard interaktif menggunakan Streamlit**.

---

## 🎯 Tujuan Proyek

Tujuan utama dari proyek ini adalah:
1. Melakukan **Exploratory Data Analysis (EDA)** untuk memahami karakteristik data transaksi e-commerce.
2. Menganalisis **performa logistik** dan dampaknya terhadap kepuasan pelanggan.
3. Mengidentifikasi **distribusi aktivitas seller** antar wilayah.
4. Melakukan **analisis lanjutan tanpa machine learning**, seperti:
   - RFM Analysis
   - Manual Grouping
   - Binning
5. Menyajikan hasil analisis dalam **dashboard interaktif**.

---

## ❓ Pertanyaan Bisnis

Analisis ini difokuskan untuk menjawab pertanyaan berikut:
1. Kategori produk mana yang memiliki penjualan rendah?
2. Negara bagian mana yang memiliki aktivitas seller tertinggi?
3. Bagaimana hubungan keterlambatan pengiriman dengan skor ulasan pelanggan?
4. State mana yang paling sering mengalami keterlambatan pengiriman?

---

## 📁 Struktur Direktori

```text
submission/
├── dashboard/
│   ├── dashboard.py        # Dashboard Streamlit
│   └── main_data.csv       # Data utama hasil penggabungan
│
├── data/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── olist_order_reviews_dataset.csv
│
├── notebook.ipynb          # Notebook analisis data (sudah dijalankan)
├── README.md               # Dokumentasi proyek
├── requirements.txt        # Daftar library yang digunakan
└── url.txt                 # (Opsional) Tautan dashboard jika dideploy
```

---

🧪 Alur Analisis Data
1. Gathering Data
Memuat dataset mentah dari beberapa tabel Olist.
2. Assessing Data
Pemeriksaan struktur data, tipe data, missing value, dan duplikasi.
3. Cleaning Data
- Konversi kolom waktu ke datetime
- Pembuatan fitur delivery_time dan is_delayed
4. Data Preparation
Seluruh dataset digabungkan dan disimpan sebagai main_data.csv, yang digunakan secara konsisten pada notebook dan dashboard.
5. Exploratory Data Analysis (EDA)
Analisis kategori produk, aktivitas seller, performa pengiriman, dan review pelanggan.
6. Analisis Lanjutan (Non–Machine Learning)
- RFM Analysis
- Manual Grouping
- Binning

---

📊 Insight Utama
- Beberapa kategori produk memiliki volume penjualan yang sangat rendah.
- Aktivitas seller terkonsentrasi pada negara bagian tertentu, terutama SP.
- Keterlambatan pengiriman berkorelasi dengan penurunan skor ulasan.
- Mayoritas pelanggan termasuk kategori Regular Customer, dengan jumlah Loyal Customer yang sangat kecil.
- Sebagian besar pelanggan berada pada kategori Low Value, sementara kontribusi pendapatan terbesar berasal dari sebagian kecil pelanggan bernilai tinggi.

---

⚙️ Setup Environment
🔹 Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

🔹 Menggunakan Shell / Terminal (pipenv)
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

▶️ Menjalankan Dashboard Streamlit
Pastikan Anda berada di direktori utama proyek, lalu jalankan perintah berikut:
``` bash
streamlit run dashboard/dashboard.py
```

Dashboard dapat diakses melalui browser pada alamat: http://localhost:8501

---

🛠️ Teknologi yang Digunakan
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

---

📌 Catatan
- Proyek ini tidak menggunakan algoritma machine learning.
- Seluruh analisis dan dashboard menggunakan main_data.csv sebagai single source of truth.
- Notebook telah dijalankan dan berisi output analisis lengkap.
- Visualisasi mengikuti prinsip kejelasan dan integritas data.