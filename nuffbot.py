
# nuffbot.py
import time
import random

def show_menu():
    print("\n--- NuffBot ---")
    print("1. Sapa saya")
    print("2. Hitung mundur")
    print("3. Kalkulator sederhana")
    print("4. Motivasi hari ini")
    print("5. Keluar")

def sapa_user():
    nama = input("Siapa namamu? ")
    print(f"Halo, {nama}! Semangat terus ya 💪")

def hitung_mundur():
    angka = int(input("Mulai hitung mundur dari angka berapa? "))
    for i in range(angka, 0, -1):
        print(i)
        time.sleep(1)
    print("Boom! 💥")

def kalkulator():
    print("Kalkulator Sederhana")
    try:
        a = float(input("Masukkan angka pertama: "))
        operator = input("Pilih operator (+, -, *, /): ")
        b = float(input("Masukkan angka kedua: "))

        if operator == '+':
            hasil = a + b
        elif operator == '-':
            hasil = a - b
        elif operator == '*':
            hasil = a * b
        elif operator == '/':
            hasil = a / b if b != 0 else "Tak terhingga (pembagian dengan nol)"
        else:
            hasil = "Operator tidak dikenali"

        print(f"Hasil: {hasil}")
    except:
        print("Input tidak valid. Coba lagi.")

def motivasi():
    quotes = [
        "Jangan menyerah, awal yang kecil lebih baik daripada tidak sama sekali.",
        "Terus belajar, terus berkembang!",
        "Kegagalan adalah bagian dari proses menuju sukses.",
        "Setiap hari adalah kesempatan baru.",
        "Kamu lebih kuat dari yang kamu kira!"
    ]
    print("💡 Motivasi hari ini:")
    print(random.choice(quotes))

def main():
    while True:
        show_menu()
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == '1':
            sapa_user()
        elif pilihan == '2':
            hitung_mundur()
        elif pilihan == '3':
            kalkulator()
        elif pilihan == '4':
            motivasi()
        elif pilihan == '5':
            print("Sampai jumpa! 👋")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
