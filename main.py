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
    """Menampilkan semua catatan belajar yang telah disimpan"""
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar. Tambahkan catatan terlebih dahulu!\n")
        return
    
    print("\n=== Daftar Catatan Belajar ===")
    print("-" * 60)
    
    for i, data in enumerate(catatan, 1):
        print(f"{i}. Mapel      : {data['mapel']}")
        print(f"   Topik      : {data['topik']}")
        print(f"   Durasi     : {data['durasi']} menit")
        print("-" * 60)
    
    print()

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