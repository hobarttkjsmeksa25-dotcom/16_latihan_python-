import tkinter as tk
from tkinter import messagebox
import database as db

db.buat_tabel()

def login():
    username = entry_username.get()
    password = entry_password.get()
    if db.cek_login(username, password):
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah.")

def daftar():
    username = entry_username.get()
    password = entry_password.get()
    if username == "" or password == "":
        messagebox.showwarning("Peringatan", "Username dan password tidak boleh kosong.")
        return
    if db.daftar_user(username, password):
        messagebox.showinfo("Berhasil", "Akun berhasil dibuat! Silakan login.")
    else:
        messagebox.showerror("Gagal", "Username sudah dipakai, coba yang lain.")

window = tk.Tk()
window.title("Login - Program Bangun Datar/Bilangan")
window.geometry("300x220")
window.resizable(False, False)

label_username = tk.Label(window, text="Username")
label_username.pack(pady=(20, 0))
entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password")
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(window, show="*")
entry_password.pack()

btn_login = tk.Button(window, text="Login", command=login, width=18)
btn_login.pack(pady=(20, 5))

btn_daftar = tk.Button(window, text="Daftar Akun Baru", command=daftar, width=18)
btn_daftar.pack()

window.mainloop()