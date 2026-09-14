import ModulMatematika as math
import ModulBangunDatar as bd
import database as db

db.buat_tabel()

def menu_awal():
    while True:
        print("<============ SELAMAT DATANG ============>\n")
        pilihan = input("1. Login\n2. Daftar Akun Baru\n3. Keluar\nPilihan Anda: ")

        if pilihan == "1":
            username = input("Username: ")
            password = input("Password: ")
            if db.cek_login(username, password):
                print(f"\nLogin berhasil! Selamat datang, {username}.\n")
                return True
            else:
                print("\nUsername atau password salah. Coba lagi.\n")

        elif pilihan == "2":
            username = input("Buat Username: ")
            password = input("Buat Password: ")
            if db.daftar_user(username, password):
                print("\nAkun berhasil dibuat! Silakan login.\n")
            else:
                print("\nUsername sudah dipakai. Coba username lain.\n")

        elif pilihan == "3":
            print("Sampai jumpa!")
            exit()

        else:
            print("Pilihan tidak dikenal.\n")


if menu_awal():
    while True:
        print("<============ SELAMAT DATANG PADA PROGRAM BANGUN DATAR/BILANGAN ============>\n")
        program = input("Masukan Program yang ingin dijalankan\n Check Bilangan = 1\n Check Bangun Datar = 2\n Pilihan Anda: ")

        if program == "1":
            print("<============ Program Matematika ============>\n")
            program_mat = input("Masukan Program yang ingin dijalankan\n Check Bilangan Prima = 1\n Check Bilangan Ganjil/Genap = 2\n Pilihan Anda: ")
            if program_mat == "1":
                math.prima()
            elif program_mat == "2":
                math.ganjil_genap()
            else:
                print("Program tidak dikenal.")
                break

        elif program == "2":
            print("<============ Program Bangun Datar ============>\n")
            program_bd = input("Masukan Program yang ingin dijalankan\n Check Nilai Segitiga = 1\n Check Nilai Persegi = 2\n Check Nilai Persegi Panjang = 3\n Check NilaiLingkaran = 4\n Pilihan Anda: ")
            if program_bd == "1":
                bd.segitiga()
            elif program_bd == "2":
                bd.persegi()
            elif program_bd == "3":
                bd.persegi_panjang()
            elif program_bd == "4":
                bd.lingkaran()
            else:
                print("Program tidak dikenal.")
            