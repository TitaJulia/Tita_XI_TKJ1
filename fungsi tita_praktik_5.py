#Nama           :Tita Julia Agatha
#Kelas          :XI-TKJ 1
#Nomor Absen    :25
#Soal           :Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
#Rumus          :Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def fibonacci(n):
    if n <= 0:
        return "Input harus merupakan bilangan bulat positif"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
hasil = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah: {hasil}")