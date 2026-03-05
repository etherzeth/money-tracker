import json
import os

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"gaji": 0, "pengeluaran": []}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def input_spend(data):
    if data["gaji"] == 0:
        data["gaji"] = int(input("Masukan gaji/budget bulan ini: Rp "))

    nominal = int(input("Nominal pengeluaran: Rp "))
    kategori = input("Kategori (makan/transport/jajan/berlangganan/lainnya): ")

    data["pengeluaran"].append({
        "nominal": nominal,
        "kategori": kategori
    })

    save_data(data)
    print(f"✓ Rp {nominal:,} untuk '{kategori}' berhasil dicatat.\n")

def show_summary(data):
    # 1. Ambil list pengeluaran dari data["pengeluaran"]
    # 2. Kalau kosong, print "belum ada data" dan stop
    # 3. Loop pengeluaran, grouping per kategori ke dictionary summary
    # 4. Hitung total semua nominal
    # 5. Ambil gaji dari data["gaji"]
    # 6. Hitung sisa = gaji - total
    # 7. Print semua kategori dan nominalnya
    # 8. Print total, budget, sisa

    pengeluaran = data["pengeluaran"]
    
    if not pengeluaran:
        print("Belum ada data pengeluaran.\n")
        return

    summary = {}

    for item in pengeluaran:
        kat = item["kategori"]
        nom = item["nominal"]

        if kat not in summary:
            summary[kat] = 0
        summary[kat] += nom
    
    print("\n=== PENGELUARAN ====")

    total = 0
    for kat, nom in summary.items():
        print(f"{kat:<15}: Rp {nom:,}")
        total += nom
    
    gaji = data["gaji"]
    sisa = gaji - total

    print("-"*29)
    print(f"{'TOTAL':<15}: Rp {total:,}")
    print(f"{'BUDGET':<15}: Rp {gaji:,}")
    print(f"{'SISA':<15}: Rp {sisa:,}")


def hapus_terakhir(data):
    if not data:
        print("Tidak ada Data untuk dihapus.\n")
        return

    hapus = data["pengeluaran"].pop()
    save_data(data)
    print(f"Data '{hapus['kategori']}' Rp {hapus['nominal']:,} berhasil dihapus.\n")

def edit_gaji(data):
    print(f"Gaji anda saat ini: Rp {data['gaji']:,}")

    new_gaji = int(input("Masukan gaji baru: Rp "))
    data['gaji'] = new_gaji
    save_data(data)
    
    print(f"Gaji anda berhasil diperbarui menjadi Rp {new_gaji:,}\n")

def main():
    data = load_data()
    while True:
        print("=== TRACKER OUT ====")
        print("1. Input pengeluaran")
        print("2. Lihat summary")
        print("3. Hapus Data")
        print("4. Edit Gaji")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            input_spend(data)
        elif pilihan == "2":
            show_summary(data)
        elif pilihan == "3":
            hapus_terakhir(data)
        elif pilihan == "4":
            edit_gaji(data)
        elif pilihan == "5":
            print("Sampai jumpa, Terimakasih sudah menggunakan tracker!")
            break
        else:
            print("Pilihan tidak valid.\n")

main()