def calon_ketua(list_calon):
    print("Daftar Calon Ketua:")
    for c in list_calon:
        print(c["id"], "-", c["nama"])
        print("Visi:", c["visi"])
        print("Misi:", c["misi"])
        print("Jumlah Suara:", c["jumlah_suara"])
        print()  

def cari_calon(list_calon, id_calon):
    for c in list_calon:
        if c["id"] == id_calon:
            return c
    return None  

def tambah_suara(list_calon, id_calon):
    for c in list_calon:
        if c["id"] == id_calon:
            c["jumlah_suara"] += 1
            break 