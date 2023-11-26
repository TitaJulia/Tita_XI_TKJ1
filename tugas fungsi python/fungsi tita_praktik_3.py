#Nama           :Tita Julia Agatha
#Kelas          :XI-TKJ 1
#Nomor Absen    :25
#Soal           :Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.
#Rumus          :Bilangan^Eksponen

def pangkat(bilangan, eksponen):
    return bilangan ** eksponen

# Contoh penggunaan
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
hasil = pangkat(bilangan, eksponen)
print(f"Hasil dari {bilangan}^ {eksponen} adalah: {hasil}")