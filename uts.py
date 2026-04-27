import os
import time

import pandas as pd
import psycopg2


DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")


def connect_db(max_retries=10, delay=3):
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            print("Berhasil konek ke database!")
            return conn
        except Exception:
            print(f"Menunggu database... ({i + 1}/{max_retries})")
            time.sleep(delay)

    print("Gagal konek ke database!")
    exit()


conn = connect_db()
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS penjualan (
        id SERIAL PRIMARY KEY,
        nama_menu TEXT,
        harga INT,
        jumlah INT,
        total INT
    )
    """
)

data_penjualan = [
    ("Ayam Geprek", 18000, 2),
    ("Nasi Goreng Seafood", 20000, 1),
    ("Es Jeruk", 7000, 3),
    ("Bakso", 15000, 2),
]

for nama, harga, jumlah in data_penjualan:
    total = harga * jumlah
    cur.execute(
        "INSERT INTO penjualan (nama_menu, harga, jumlah, total) "
        "VALUES (%s, %s, %s, %s)",
        (nama, harga, jumlah, total),
    )

conn.commit()

cur.execute("SELECT SUM(total) FROM penjualan")
total_penjualan = cur.fetchone()[0]

cur.execute(
    """
    SELECT nama_menu, SUM(jumlah)
    FROM penjualan
    GROUP BY nama_menu
    ORDER BY SUM(jumlah) DESC
    LIMIT 1
    """
)
menu_terlaris = cur.fetchone()

cur.execute("SELECT AVG(total) FROM penjualan")
rata_rata = cur.fetchone()[0]

print("\n=== LAPORAN PENJUALAN RUMAH MAKAN ===")
print("Total Penjualan       : Rp", total_penjualan)
print(
    "Menu Terlaris         :",
    menu_terlaris[0],
    "-",
    menu_terlaris[1],
    "terjual",
)
print("Rata-rata Transaksi   : Rp", int(rata_rata))

print("\nDetail Data:")
cur.execute("SELECT * FROM penjualan")
rows = cur.fetchall()

for row in rows:
    print(row)

colnames = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows, columns=colnames)
df.to_csv("data_penjualan.csv", index=False)

print("\nData berhasil disimpan ke file: data_penjualan.csv")

cur.close()
conn.close()