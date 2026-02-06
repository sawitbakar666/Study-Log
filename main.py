import json
from datetime import datetime

catatan = []
target_harian = 120  # Default 120 menit per hari

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
    
    # Simpan ke dalam list sebagai dictionary dengan tanggal
    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M")
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
    """Menghitung dan menampilkan total waktu belajar"""
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar. Tambahkan catatan terlebih dahulu!\n")
        return
    
    # Hitung total durasi
    total_durasi = sum(data['durasi'] for data in catatan)
    
    # Konversi ke jam dan menit
    jam = total_durasi // 60
    menit = total_durasi % 60
    
    print("\n=== Total Waktu Belajar ===")
    print(f"Total durasi: {total_durasi} menit")
    print(f"Atau: {jam} jam {menit} menit")
    print(f"Jumlah catatan: {len(catatan)}\n")

def filter_per_mapel():
    """Menampilkan catatan belajar yang difilter per mapel"""
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar.\n")
        return
    
    # Dapatkan daftar mapel unik
    mapel_unik = list(set(data['mapel'] for data in catatan))
    
    print("\n=== Daftar Mapel ===")
    for i, mapel in enumerate(mapel_unik, 1):
        print(f"{i}. {mapel}")
    
    try:
        pilihan = int(input("Pilih nomor mapel: ")) - 1
        if 0 <= pilihan < len(mapel_unik):
            mapel_terpilih = mapel_unik[pilihan]
            catatan_mapel = [data for data in catatan if data['mapel'] == mapel_terpilih]
            
            print(f"\n=== Catatan untuk {mapel_terpilih} ===")
            print("-" * 60)
            for i, data in enumerate(catatan_mapel, 1):
                print(f"{i}. Topik      : {data['topik']}")
                print(f"   Durasi     : {data['durasi']} menit")
                print(f"   Tanggal    : {data['tanggal']}")
                print("-" * 60)
            
            total = sum(data['durasi'] for data in catatan_mapel)
            print(f"Total waktu {mapel_terpilih}: {total} menit\n")
        else:
            print("Pilihan tidak valid!\n")
    except ValueError:
        print("Masukkan angka yang valid!\n")

def set_target_harian():
    """Mengatur target waktu belajar harian"""
    global target_harian
    
    print(f"\nTarget harian saat ini: {target_harian} menit")
    try:
        target_baru = int(input("Masukkan target harian baru (menit): "))
        if target_baru > 0:
            target_harian = target_baru
            print(f"✓ Target harian berhasil diubah menjadi {target_harian} menit\n")
        else:
            print("Target harus lebih dari 0!\n")
    except ValueError:
        print("Masukkan angka yang valid!\n")

def cek_target_harian():
    """Mengecek apakah target harian sudah tercapai"""
    total_hari_ini = sum(data['durasi'] for data in catatan 
                        if datetime.now().strftime("%Y-%m-%d") in data['tanggal'])
    
    print(f"\n=== Cek Target Harian ===")
    print(f"Target: {target_harian} menit")
    print(f"Tercapai: {total_hari_ini} menit")
    
    if total_hari_ini >= target_harian:
        persentase = 100
        print(f"Status: ✓ Tercapai ({persentase}%)\n")
    else:
        sisa = target_harian - total_hari_ini
        persentase = (total_hari_ini / target_harian) * 100
        print(f"Status: Kurang {sisa} menit ({persentase:.1f}%)\n")

def simpan_ke_file():
    """Menyimpan semua catatan ke file JSON"""
    if len(catatan) == 0:
        print("\n⚠ Tidak ada catatan untuk disimpan.\n")
        return
    
    nama_file = input("Masukkan nama file (tanpa .json): ").strip()
    if not nama_file:
        nama_file = "study_log"
    
    nama_file = f"{nama_file}.json"
    
    try:
        with open(nama_file, 'w') as f:
            json.dump(catatan, f, indent=2)
        print(f"✓ Catatan berhasil disimpan ke {nama_file}\n")
    except Exception as e:
        print(f"✗ Gagal menyimpan file: {e}\n")

def muat_dari_file():
    """Memuat catatan dari file JSON"""
    global catatan
    
    nama_file = input("Masukkan nama file (tanpa .json): ").strip()
    if not nama_file:
        nama_file = "study_log"
    
    nama_file = f"{nama_file}.json"
    
    try:
        with open(nama_file, 'r') as f:
            catatan = json.load(f)
        print(f"✓ Catatan berhasil dimuat dari {nama_file} ({len(catatan)} catatan)\n")
    except FileNotFoundError:
        print(f"✗ File {nama_file} tidak ditemukan.\n")
    except Exception as e:
        print(f"✗ Gagal memuat file: {e}\n")

def ringkasan_mingguan():
    """Menampilkan ringkasan catatan belajar"""
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar.\n")
        return
    
    print("\n=== Ringkasan Belajar ===")
    print("-" * 60)
    
    # Total waktu
    total_durasi = sum(data['durasi'] for data in catatan)
    jam = total_durasi // 60
    menit = total_durasi % 60
    
    # Mapel yang paling banyak dipelajari
    mapel_durasi = {}
    for data in catatan:
        mapel_durasi[data['mapel']] = mapel_durasi.get(data['mapel'], 0) + data['durasi']
    
    mapel_terbanyak = max(mapel_durasi, key=mapel_durasi.get) if mapel_durasi else "-"
    waktu_terbanyak = mapel_durasi.get(mapel_terbanyak, 0) if mapel_terbanyak != "-" else 0
    
    print(f"Total waktu belajar: {total_durasi} menit ({jam}h {menit}m)")
    print(f"Total catatan: {len(catatan)}")
    print(f"Mapel terbanyak: {mapel_terbanyak} ({waktu_terbanyak} menit)")
    print(f"Rata-rata per catatan: {total_durasi // len(catatan)} menit")
    print("-" * 60)
    
    print("\nRingkasan per mapel:")
    for mapel, durasi in sorted(mapel_durasi.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {mapel}: {durasi} menit")
    print()

def menu():
    print("\n=== Study Log App ===")
    print("📚 Menu Utama:")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("\n🎯 Pengembangan Mandiri:")
    print("4. Filter per mapel")
    print("5. Cek target harian")
    print("6. Ringkasan belajar")
    print("7. Pengaturan & File")
    print("8. Keluar")

def menu_pengaturan():
    """Submenu untuk pengaturan dan penyimpanan file"""
    while True:
        print("\n=== Pengaturan & File ===")
        print("1. Set target harian")
        print("2. Cek target harian")
        print("3. Simpan ke file")
        print("4. Muat dari file")
        print("5. Kembali ke menu utama")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            set_target_harian()
        elif pilihan == "2":
            cek_target_harian()
        elif pilihan == "3":
            simpan_ke_file()
        elif pilihan == "4":
            muat_dari_file()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")

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
        filter_per_mapel()
    elif pilihan == "5":
        cek_target_harian()
    elif pilihan == "6":
        ringkasan_mingguan()
    elif pilihan == "7":
        menu_pengaturan()
    elif pilihan == "8":
        print("\nTerima kasih, terus semangat belajar! 🎓")
        break
    else:
        print("Pilihan tidak valid")