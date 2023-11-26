#Nama   :Tita Julia Agatha
#Kelas  :XI-TKJ 1
#Absen  :25
#Soal   :Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.
#Rumus  :Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke- (n-1)

investasi_awal = 10000  # Nilai investasi awal dalam dollar
target_investasi = 20000  # Nilai investasi yang diinginkan dalam dollar
tingkat_pertumbuhan = 0.06  # Tingkat pertumbuhan 6% setiap tahun
tahun = 0  # Inisialisasi jumlah tahun

while investasi_awal <= target_investasi:
    tahun += 1
    investasi_awal += investasi_awal * tingkat_pertumbuhan  # Pertumbuhan 6% setiap tahun

print("Jumlah tahun yang dibutuhkan:", tahun)