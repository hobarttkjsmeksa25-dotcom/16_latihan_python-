"""
Program Menghitung Luas Persegi Panjang dengan perulangan
"""

while True:
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan GENAP")
    else:
        print(f"{angka} adalah bilangan GANJIL")

    ulang = input("\nMau coba lagi? (y/n): ")

    if ulang.lower() == "n":
        print("Program selesai. Terima kasih!")
        break
