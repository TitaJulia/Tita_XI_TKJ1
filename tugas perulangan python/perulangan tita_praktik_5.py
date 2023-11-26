#Nama   :Tita Juia Agatha
#Kelas  :XI-TKJ 1
#Absen  :25
#Soal   :Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.
#Rumus  :Jumlah pembelahan setelah t menit = t / 20

waktu_total_menit = 120  # Rentang waktu dalam menit
waktu_pembelahan_menit = 20  # Waktu pembelahan setiap 20 menit
jumlah_pembelahan = waktu_total_menit // waktu_pembelahan_menit

print("Jumlah pembelahan bakteri dalam 2 jam:", jumlah_pembelahan)