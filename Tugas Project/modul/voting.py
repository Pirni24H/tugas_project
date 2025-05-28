from modul import pemilih, calon

def proses_voting(list_pemilih, list_calon):
    print("\n==== VOTING ====")
    id_pemilih = input("Masukkan ID Pemilih: ")

    data_pemilih = pemilih.fiks_pemilih(list_pemilih, id_pemilih)

    if data_pemilih is None:
        print("Pemilih tidak ditemukan.")
        return

    if data_pemilih["sudah_memilih"]:
        print("Pemilih sudah melakukan voting.")
        return

    calon.calon_ketua(list_calon)  #
    id_calon = input("Masukkan ID Calon yang dipilih: ")
    data_calon = calon.cari_calon(list_calon, id_calon)

    if data_calon is None:
        print("Calon tidak ditemukan.")
        return

    calon.tambah_suara(list_calon, id_calon)
    pemilih.tanda_jika_sudahmemilih(list_pemilih, id_pemilih)

    print("Voting berhasil, terima kasih.")

def hasil_sementara(list_calon):
    print("\n===== Hasil Sementara =====")
    calon.calon_ketua(list_calon)
