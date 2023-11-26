#Nama           :Tita Julia Agatha
#Kelas          :XI-TKJ 1
#Nomor Absen    :25
#Soal           :Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.
#Rumus          :Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, batas + 1, 2):
        total += i
    return total

# Contoh penggunaan
batas = int(input("Masukkan batas deret: "))
hasil = total_deret_ganjil(batas)
print(f"Total deret ganjil hingga batas {batas} adalah: {hasil}")