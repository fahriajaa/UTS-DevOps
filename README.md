# Aplikasi Analisis Penjualan Rumah Makan (DevOps)

##  Deskripsi

Project ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk:

* Mengelola data penjualan rumah makan
* Menyimpan data ke database PostgreSQL
* Melakukan analisis sederhana (total penjualan, menu terlaris, rata-rata transaksi)
* Mengekspor data ke file CSV

Project ini juga telah diintegrasikan dengan:

* Docker & Docker Compose
*  GitHub Actions (CI Pipeline)

---

## Teknologi yang Digunakan

* Python 3.9
* PostgreSQL
* Docker
* Docker Compose
* Pandas
* psycopg2
* GitHub Actions

---

##  Struktur Project

```
.
├── uts.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── data_penjualan.csv
└── .github/
    └── workflows/
        └── main.yml
```

---

## Cara Menjalankan Project

### 1. Clone Repository

```
git clone https://github.com/username/UTS-DevOps.git
cd UTS-DevOps
```

---

### 2. Jalankan dengan Docker

```
docker-compose up --build
```

---

### 3. Hasil Output

Program akan menampilkan:

* Total penjualan
* Menu terlaris
* Rata-rata transaksi
* Detail data

Selain itu, file CSV akan otomatis dibuat:
```
data_penjualan.csv
```
##  Fitur Utama

###  Koneksi Database dengan Retry

Aplikasi akan menunggu database siap sebelum terhubung.

###  Insert Data Otomatis

Data penjualan dimasukkan ke database secara otomatis.

###  Analisis Data

* Total penjualan
* Menu terlaris
* Rata-rata transaksi

### Export ke CSV

Data disimpan dalam format CSV menggunakan Pandas.

## CI/CD (GitHub Actions)

Project ini menggunakan GitHub Actions untuk:

* Install dependencies
* Menjalankan linting dengan flake8

Workflow akan berjalan otomatis saat push ke branch `main`.

## Contoh Output

*LAPORAN PENJUALAN RUMAH MAKAN*
Total Penjualan       : Rp 107000
Menu Terlaris         : Ayam Geprek - 2 terjual
Rata-rata Transaksi   : Rp 26750

## Author

* Nama: Fahri Akbar
* Mata Kuliah: DevOps for Data Science
