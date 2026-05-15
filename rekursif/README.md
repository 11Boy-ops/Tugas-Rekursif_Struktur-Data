# 🧩 Tugas Rekursif — Algoritma Backtracking

Repositori ini berisi implementasi tiga algoritma rekursif klasik dalam ilmu komputer sebagai jawaban tugas pemrograman rekursif.

---

## 📁 Struktur Direktori

```
README.md
rekursif/
├── n-queens/
│   └── n_queens.py          # Soal 1: N-Queens Problem
├── knights-tour/
│   └── knights_tour.py      # Soal 2: Knight's Tour
└── knapsack/
    └── knapsack.py          # Soal 3: Knapsack Problem
```

---

## ⚙️ Cara Menjalankan

Pastikan Python 3.x sudah terinstal:

```bash
python3 --version
```

Masuk ke direktori proyek terlebih dahulu:

```bash
cd rekursif
```

Jalankan setiap program dengan perintah:

```bash
# Soal 1
python3 n-queens/n_queens.py

# Soal 2
python3 knights-tour/knights_tour.py

# Soal 3
python3 knapsack/knapsack.py
```

---

## 📌 Soal 1 — N-Queens (N-Ratu)

### Deskripsi
Tempatkan **N ratu** di papan catur **N×N** sehingga tidak ada dua ratu yang saling menyerang satu sama lain (tidak ada dua ratu yang berada di baris, kolom, atau diagonal yang sama).

### Algoritma: Backtracking Rekursif

```
solve(board, baris):
    JIKA baris == N → simpan solusi (BASE CASE)
    UNTUK setiap kolom dari 0 sampai N-1:
        JIKA aman menempatkan ratu di (baris, kolom):
            tempatkan ratu
            solve(board, baris + 1)   ← REKURSI
            hapus ratu (BACKTRACK)
```

**Cara cek posisi aman:** Periksa apakah ada ratu lain di:
- Kolom yang sama (ke atas)
- Diagonal kiri atas
- Diagonal kanan atas

### Contoh Output (N=4)

```
  Solusi #1:
  +---+---+---+---+
  |   | Q |   |   |  ← baris 1
  +---+---+---+---+
  |   |   |   | Q |  ← baris 2
  +---+---+---+---+
  | Q |   |   |   |  ← baris 3
  +---+---+---+---+
  |   |   | Q |   |  ← baris 4
  +---+---+---+---+
  Posisi ratu (per baris): [2, 4, 1, 3]
```

| N | Jumlah Solusi |
|---|--------------|
| 4 | 2            |
| 5 | 10           |
| 6 | 4            |
| 8 | 92           |

---

## 📌 Soal 2 — Knight's Tour (Tur Kuda)

### Deskripsi
Temukan urutan langkah kuda catur sehingga setiap petak di papan **N×N** dikunjungi **tepat satu kali**. Kuda bergerak dalam pola huruf "L" (2 petak + 1 petak menyamping).

### Algoritma: Backtracking Rekursif + Heuristik Warnsdorff

```
solve(board, baris, kolom, langkah_ke):
    JIKA langkah_ke == N×N → solusi ditemukan (BASE CASE)
    kumpulkan semua langkah valid dari posisi ini
    urutkan berdasarkan heuristik Warnsdorff (sedikit pilihan dulu)
    UNTUK setiap langkah:
        pindahkan kuda
        solve(board, baru_baris, baru_kolom, langkah_ke+1)  ← REKURSI
        batalkan langkah (BACKTRACK) jika gagal
```

**Heuristik Warnsdorff:** Selalu prioritaskan bergerak ke petak yang memiliki **paling sedikit** kemungkinan langkah berikutnya. Ini drastis mengurangi jumlah backtracking yang dibutuhkan.

### 8 Gerakan Legal Kuda

```
    .  X  .  X  .
    X  .  .  .  X
    .  .  ♞  .  .
    X  .  .  .  X
    .  X  .  X  .
```

Offset gerakan: `(-2,-1), (-2,+1), (-1,-2), (-1,+2), (+1,-2), (+1,+2), (+2,-1), (+2,+1)`

### Contoh Output (6×6, mulai dari baris 1, kolom A)

```
  Papan (angka = urutan kunjungan):
  +----+----+----+----+----+----+
  | 1  | 28 | 9  | 20 | 3  | 30 |
  +----+----+----+----+----+----+
  | 10 | 21 | 2  | 29 | 16 | 19 |
  ...
```

---

## 📌 Soal 3 — Knapsack Problem (Masalah Karung)

### Deskripsi
Diberikan sebuah tas dengan kapasitas berat tertentu dan sekumpulan barang dengan berat berbeda-beda. Temukan kombinasi barang yang totalnya **tepat sama** dengan berat target (tidak boleh melebihi).

### Algoritma: Rekursi dengan Backtracking

```
knapsack(barang[], indeks, sisa_berat, kombinasi_saat_ini):
    JIKA sisa_berat == 0 → SIMPAN SOLUSI (BASE CASE ✓)
    JIKA indeks >= len(barang) atau sisa_berat < 0 → BERHENTI (BASE CASE ✗)
    
    // PILIHAN 1: MASUKKAN barang ke-indeks
    JIKA barang[indeks] <= sisa_berat:
        masukkan barang[indeks] ke kombinasi
        knapsack(barang, indeks+1, sisa_berat - barang[indeks], kombinasi)  ← REKURSI
        keluarkan barang[indeks]  ← BACKTRACK
    
    // PILIHAN 2: LEWATI barang ke-indeks
    knapsack(barang, indeks+1, sisa_berat, kombinasi)  ← REKURSI
```

### Contoh Output

```
Daftar barang : [2, 5, 6, 9, 12, 14, 20]
Berat target  : 30

✓ SOLUSI DITEMUKAN!

  Solusi #1: [2, 5, 9, 14]
            Total berat = 30 (target = 30)
            Barang tidak masuk: [6, 12, 20]
```

---

## 🔑 Konsep Kunci: Backtracking

Ketiga program menggunakan pola **backtracking** yang sama:

```
def solve(state):
    if goal_reached(state):        # BASE CASE: tujuan tercapai
        save_solution()
        return True
    
    for choice in get_choices():   # Coba semua pilihan
        make_choice(state, choice) # Lakukan pilihan
        if solve(state):           # REKURSI
            return True
        undo_choice(state, choice) # BACKTRACK: batalkan jika gagal
    
    return False
```

**Rekursi = membagi masalah besar menjadi sub-masalah yang lebih kecil**  
**Backtracking = membatalkan pilihan yang tidak mengarah ke solusi**

---

## 👤 Informasi

| Item | Detail |
|------|--------|
| Mata Kuliah | Struktur Data |
| Topik | Rekursi & Backtracking |
| Bahasa | Python 3 |
| Algoritma | N-Queens, Knight's Tour, Knapsack |
