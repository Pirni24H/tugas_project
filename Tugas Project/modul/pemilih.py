def pemilih(list_pemilih):
    print("Daftar pemilih :")
    for p in list_pemilih:
        if p["sudah_memilih"]:
            status = "Sudah Memilih"
        else:
            status = "Belum Memilih"
        print(p["id"], "-", p["nama"])
        print(p["jurusan"], "-", status)

def fiks_pemilih(list_pemilih, id_pemilih):
    for p in list_pemilih:
        if p["id"] == id_pemilih:
            return p
    return None  

def tanda_jika_sudahmemilih(list_pemilih, id_pemilih):
    for p in list_pemilih:
        if p["id"] == id_pemilih:
            p["sudah_memilih"] = True
