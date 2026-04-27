import psycopg2
import time

# Fungsi koneksi (pakai retry biar tidak error saat DB belum siap)
def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",          # untuk Docker
                database="testdb",
                user="user",
                password="password"
            )
            return conn
        except:
            print("Menunggu database siap...")
            time.sleep(3)

conn = connect_db()
cur = conn.cursor()

# Buat tabel
cur.execute("""
CREATE TABLE IF NOT EXISTS penjualan (
    id SERIAL PRIMARY KEY,
    nama_menu TEXT,
    harga INT,
    jumlah INT,
    total INT
)
""")

# Data penjualan (bisa kamu ubah biar beda dari teman)
data_penjualan = [
    ("Ayam Geprek", 18000, 2),
    ("Nasi Goreng Seafood", 20000, 1),
    ("Es Jeruk", 7000, 3),
    ("Bakso", 15000, 2)
]

# Insert data
for nama, harga, jumlah in data_penjualan:
    total = harga * jumlah
    cur.execute(
        "INSERT INTO penjualan (nama_menu, harga, jumlah, total) VALUES (%s, %s, %s, %s)",
        (nama, harga, jumlah, total)
    )

conn.commit()

# ======================
# 📊 ANALISIS SEDERHANA
# ======================

# Total penjualan
cur.execute("SELECT SUM(total) FROM penjualan")
total_penjualan = cur.fetchone()[0]

# Menu terlaris (berdasarkan jumlah)
cur.execute("""
SELECT nama_menu, SUM(jumlah) as total_jual
FROM penjualan
GROUP BY nama_menu
ORDER BY total_jual DESC
LIMIT 1
""")
menu_terlaris = cur.fetchone()

# Rata-rata transaksi
cur.execute("SELECT AVG(total) FROM penjualan")
rata_rata = cur.fetchone()[0]

# ======================
# OUTPUT
# ======================

print("\n=== LAPORAN PENJUALAN RUMAH MAKAN ===")
print("Total Penjualan       : Rp", total_penjualan)
print("Menu Terlaris         :", menu_terlaris[0], "-", menu_terlaris[1], "terjual")
print("Rata-rata Transaksi   : Rp", int(rata_rata))

print("\nDetail Data:")
cur.execute("SELECT * FROM penjualan")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()