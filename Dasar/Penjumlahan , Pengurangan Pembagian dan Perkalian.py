def sum(a, b, c):
    return a + b + c

def subtract(a, b, c):
    return a - b - c

def multiply(a, b, c):
    return a * b * c

def divide(a, b, c):
    return a / b / c

# Meminta input dari pengguna setelah mendefinisikan variabel a dan b
a = int(input('Masukkan angka pertama: '))
b = int(input('Masukkan angka kedua: '))
c = int(input('Masukkan angka kedua : '))

# Melakukan operasi matematika
sum_result = sum(a, b, c)
subtract_result = subtract(a, b, c)
multiply_result = multiply(a, b, c)
divide_result = divide(a, b, c)

# Menampilkan hasil
print(f'Penjumlahan dari {a},{b} dan {c} adalah {sum_result}')
print(f'Pengurangan dari {a},{b} dan {c} adalah {subtract_result}')
print(f'Perkalian dari {a}, {b} dan {c} adalah {multiply_result}')
print(f'Pembagian dari {a}, {b} dan {c} adalah {divide_result}')
