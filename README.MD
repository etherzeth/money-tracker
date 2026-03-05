# MONEY TRACKER

## 1. Deskripsi

**Money Tracker** adalah program sederhana berbasis Python yang digunakan untuk mencatat dan memantau pengeluaran bulanan berdasarkan kategori serta membandingkannya dengan budget atau gaji yang dimiliki.

Program ini berjalan di terminal (command line) dan menyimpan semua data pengeluaran ke dalam file `data.json` agar data tetap tersimpan walaupun program ditutup.

---

## 2. Fitur

Program ini memiliki beberapa fitur utama:

* **Input Pengeluaran**
  Menambahkan data pengeluaran dengan nominal dan kategori.

* **Summary Pengeluaran**
  Menampilkan ringkasan pengeluaran berdasarkan kategori.

* **Perhitungan Total Pengeluaran**
  Menghitung total seluruh pengeluaran yang sudah dicatat.

* **Perhitungan Sisa Budget**
  Menghitung sisa uang dari budget atau gaji setelah dikurangi pengeluaran.

* **Hapus Data Terakhir**
  Menghapus data pengeluaran terakhir yang dimasukkan.

* **Edit Gaji / Budget**
  Mengubah nilai gaji atau budget bulanan.

* **Penyimpanan Otomatis ke File JSON**
  Semua data pengeluaran disimpan di file `data.json`, sehingga data tidak hilang ketika program ditutup.

---

## 3. Cara Install

### Persiapan

Pastikan sudah menginstall:

* **Python 3.8 atau lebih baru**
  (Direkomendasikan menggunakan Python **3.12** atau versi terbaru)

Cek versi Python dengan perintah berikut di terminal:

```
python --version
```

atau

```
python3 --version
```

### Library yang Dibutuhkan

Program ini **tidak memerlukan library tambahan** karena hanya menggunakan modul bawaan Python:

* `json`
* `os`

---

## 4. Cara Pakai

1. Download atau clone repository ini.
2. Masuk ke folder project melalui terminal.
3. Jalankan program dengan perintah berikut:

```
python tracker.py
```

atau

```
python3 tracker.py
```

Setelah program berjalan, akan muncul menu seperti berikut:

```
=== TRACKER OUT ====
1. Input pengeluaran
2. Lihat summary
3. Hapus Data
4. Edit Gaji
5. Keluar
```

Gunakan angka pada menu untuk memilih fitur:

* `1` → Input pengeluaran
* `2` → Melihat summary pengeluaran
* `3` → Menghapus data terakhir
* `4` → Mengedit gaji / budget
* `5` → Keluar dari program

Semua data pengeluaran akan otomatis tersimpan dalam file **data.json**.

----