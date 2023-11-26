#Nama   :Tita Julia Agatha
#Kelas  :XI-TKJ 1
#Absen  :25
#Soal   :Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.
#Rumus  :Jarak minggu ke-n = Jarak minggu ke-(n-1) + 10% dari Jarak minggu ke-(n-1)

jarak_awal = 5  # Jarak awal
target_jarak = 10  # Jarak yang diinginkan
persentase_kenaikan = 10/100 #Meningkat 10% setiap minggu
minggu = 0  # awalan jumlah minggu

while jarak_awal <= target_jarak:
    minggu += 1
    jarak_awal += jarak_awal * persentase_kenaikan

print("Jumlah minggu yang dibutuhkan:", minggu)

#10-5 = 5
#10% * 5 = 0.5
#5 dibagi 0.5 = 10
#jadi butuh 10 minggu untuk bisa meningkatkan jarak tempuh menjadi 10 kilometer
#Tapi kenapa saat di run jawabannya hanay 8 minggu ?