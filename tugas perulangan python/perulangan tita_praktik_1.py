#Nama   :Tita Julia Agatha
#Kelas  :XI-TKJ 1
#Absen  :25
#Soal   :Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.
#Rumus  :Jumlah ayam bulan ke-n = Jumlah ayam bulan ke-(n-1) + 5% dari Jumlah ayam bulan ke-(n-1)

jumlah_ayam = 100  # Jumlah awal
target_ayam = 200  # Jumlah yang diinginkan
bulan = 0  # awalan jumlah bulan

while jumlah_ayam <= target_ayam:
    bulan += 1
    jumlah_ayam += jumlah_ayam * 5/100

print("Jumlah bulan yang dibutuhkan:", bulan)

#Penjelasan
#Jumlah ayam = 100
#target ayam = 200 atau lebih
#100 : 5% = 20
#Jika target 200 maka 20*5 = 100+100(jumlah ayam awal) = 200(target)
#jawaban bulan yang dibutuhkan = 15 * 20(5% per bulan) = 250 ayam
#Belum paham cara menargetkan tepat 200 ayam(rama)