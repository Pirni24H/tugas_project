def statistik(list_pemilih, list_calon):
    total_pemilih = len(list_pemilih)
    jumlah_memilih = 0

    for p in list_pemilih:
        if p["sudah_memilih"]:
            jumlah_memilih += 1

    if total_pemilih > 0:
        persentase = (jumlah_memilih / total_pemilih) * 100
    else:
        persentase = 0

    suara_terbanyak = 0
    calon_teratas = ""

    for c in list_calon:
        if c["jumlah_suara"] > suara_terbanyak:
            suara_terbanyak = c["jumlah_suara"]
            calon_teratas = c["nama"]

    print("\n===== Statistik Pemilih ======")
    print("Total Pemilih         :", total_pemilih)
    print("Sudah Memilih         :", jumlah_memilih)
    print("Partisipasi Pemilih   : {:.2f}%".format(persentase))
    print("Calon dengan suara terbanyak :", calon_teratas, "dengan", suara_terbanyak, "suara")
