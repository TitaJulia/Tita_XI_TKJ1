#Nama   :Tita Julia Agatha
#Kelas  :XI-TKJ 1
#Absen  :25
#Soal   :Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.
#Rumus  :Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)

jumlah_apel = 100  # Jumlah apel awal
batas_apel = 20  # Jumlah apel yang diinginkan sebagai batas
persentase_penjualan = 0.10  # Persentase penjualan 10% setiap hari
hari = 0  # Inisialisasi jumlah hari

while jumlah_apel > batas_apel:
    hari += 1
    jumlah_penjualan = jumlah_apel * persentase_penjualan
    jumlah_apel -= jumlah_penjualan  # Penjualan 10% setiap hari

print("Jumlah hari yang dibutuhkan:", hari)