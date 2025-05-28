import json
import modul_pemilih as p
import modul_calon as c

def load_data():
    with open("data/pemilih.json", "r") as f:
        list_pemilih = json.load(f)
    with open("data/calon.json", "r") as f:
        list_calon = json.load(f)
    return list_pemilih, list_calon

def save_data(list_pemilih, list_calon):
    with open("data/pemilih.json", "w") as f:
        json.dump(list_pemilih, f, indent=4)
    with open("data/calon.json", "w") as f:
        json.dump(list_calon, f, indent=4)

def menu():
    list_pemilih, list_calon = load_data()

    while True:
        print("\n===== SISTEM E-VOTING KETUA ORGANISASI =====")
        print("1. Lihat Daftar Pemilih")
        print("2. Voting")
        print("3. Lihat Hasil Sementara")
        print("4. Statistik Pemilu")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            p.pemilih(list_pemilih)
        elif pilihan == "2":
            c.proses_voting(list_pemilih, list_calon)
            save_data(list_pemilih, list_calon)
        elif pilihan == "3":
            c.hasil_sementara(list_calon)
        elif pilihan == "4":
            c.statistik(list_pemilih, list_calon)
        elif pilihan == "5":
            save_data(list_pemilih, list_calon)
            print("Terima kasih telah menggunakan sistem e-voting.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()
