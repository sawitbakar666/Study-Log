catatan = []

def tambah_catatan():
    """Menambahkan catatan belajar baru ke dalam list"""
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    
    # Validasi durasi belajar
    while True:
        try:
            durasi = int(input("Masukkan durasi belajar (menit): "))
            if durasi <= 0:
                print("Durasi harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    # Simpan ke dalam list sebagai dictionary
    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    })
    print("✓ Catatan berhasil ditambahkan!\n")

def lihat_catatan():
    pass

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")