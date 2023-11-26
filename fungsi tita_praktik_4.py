#Nama           :Tita Julia Agatha
#Kelas          :XI-TKJ 1
#Nomor Absen    :25
#Soal           :Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.
#Rumus          :Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n

def jumlah_digit(bilangan):
    return len(str(abs(bilangan)))

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
hasil = jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah: {hasil}")