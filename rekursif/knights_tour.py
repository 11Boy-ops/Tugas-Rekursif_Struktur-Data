"""
=============================================================
  SOAL 2: KNIGHT'S TOUR (TUR KUDA)
  Algoritma: Backtracking Rekursif + Heuristik Warnsdorff
=============================================================
  Tujuan: Menemukan jalur kuda sehingga setiap petak di 
  papan dikunjungi tepat satu kali.
  
  Heuristik Warnsdorff: Selalu pindah ke petak yang memiliki
  paling sedikit kemungkinan langkah berikutnya (greedy),
  sehingga backtracking lebih jarang terjadi.
=============================================================
"""

# 8 kemungkinan gerakan kuda (bentuk huruf L)
MOVES = [
    (-2, -1), (-2, +1),   # 2 ke atas, 1 ke kiri/kanan
    (-1, -2), (-1, +2),   # 1 ke atas, 2 ke kiri/kanan
    (+1, -2), (+1, +2),   # 1 ke bawah, 2 ke kiri/kanan
    (+2, -1), (+2, +1),   # 2 ke bawah, 1 ke kiri/kanan
]


def is_valid_move(board, row, col, n):
    """Memeriksa apakah posisi (row, col) valid dan belum dikunjungi."""
    return 0 <= row < n and 0 <= col < n and board[row][col] == -1


def count_onward_moves(board, row, col, n):
    """
    Heuristik Warnsdorff: Hitung jumlah langkah valid
    yang tersedia dari posisi (row, col).
    """
    count = 0
    for dr, dc in MOVES:
        nr, nc = row + dr, col + dc
        if is_valid_move(board, nr, nc, n):
            count += 1
    return count


def solve_knights_tour(board, row, col, move_num, n):
    """
    Fungsi rekursif untuk menyelesaikan Knight's Tour.
    
    Base case : move_num == n*n → semua petak sudah dikunjungi
    Rekursi   : coba semua langkah valid, urutkan berdasarkan
                heuristik Warnsdorff (paling sedikit langkah berikutnya)
    """
    # BASE CASE: semua petak sudah dikunjungi
    if move_num == n * n:
        return True

    # Kumpulkan semua langkah valid dengan skornya (heuristik Warnsdorff)
    next_moves = []
    for dr, dc in MOVES:
        nr, nc = row + dr, col + dc
        if is_valid_move(board, nr, nc, n):
            # Skor = jumlah langkah dari posisi berikutnya (lebih kecil = prioritas lebih tinggi)
            score = count_onward_moves(board, nr, nc, n)
            next_moves.append((score, nr, nc))

    # Urutkan berdasarkan skor (ascending) - heuristik Warnsdorff
    next_moves.sort()

    # REKURSI: coba setiap langkah yang sudah diurutkan
    for score, nr, nc in next_moves:
        board[nr][nc] = move_num       # Tandai langkah
        if solve_knights_tour(board, nr, nc, move_num + 1, n):
            return True
        board[nr][nc] = -1             # Backtrack: hapus langkah


    return False  # Tidak ada solusi dari posisi ini


def print_board(board, n):
    """Mencetak papan dengan nomor urut kunjungan setiap petak."""
    cell_width = len(str(n * n)) + 2
    separator = "  +" + ("-" * cell_width + "+") * n

    print(separator)
    for i in range(n):
        print("  |", end="")
        for j in range(n):
            val = board[i][j] + 1  # +1 karena dimulai dari 0
            print(f"{val:^{cell_width}}|", end="")
        print()
        print(separator)


def print_path(board, n):
    """Mencetak urutan langkah kuda secara berurutan."""
    # Buat mapping dari langkah ke posisi
    path = [(0, 0)] * (n * n)
    for i in range(n):
        for j in range(n):
            path[board[i][j]] = (i, j)

    print("\n  Urutan langkah kuda:")
    for step in range(n * n):
        r, c = path[step]
        # Konversi ke notasi papan catur (kolom: A-H, baris: 1-N)
        col_letter = chr(ord('A') + c)
        row_num = r + 1
        print(f"  Langkah {step + 1:3d}: ({row_num}, {col_letter})", end="")
        if (step + 1) % 4 == 0:
            print()
    print()


def main():
    print("=" * 55)
    print("        PROGRAM KNIGHT'S TOUR (TUR KUDA)")
    print("=" * 55)
    print("Tujuan: Kuda mengunjungi setiap petak tepat satu kali.")
    print("Menggunakan algoritma Backtracking + Heuristik Warnsdorff.\n")

    while True:
        try:
            n = int(input("Masukkan ukuran papan (N, minimal 5): "))
            if n < 5:
                print("Ukuran papan minimal 5 agar ada solusi. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat positif.")

    print(f"\nUntuk papan {n}×{n}, posisi dinyatakan sebagai (baris 1-{n}, kolom A-{chr(ord('A')+n-1)})")

    while True:
        try:
            start_row = int(input(f"Masukkan baris awal kuda (1-{n}): ")) - 1
            start_col_input = input(f"Masukkan kolom awal kuda (A-{chr(ord('A')+n-1)}): ").upper()
            start_col = ord(start_col_input) - ord('A')

            if not (0 <= start_row < n and 0 <= start_col < n):
                print(f"Posisi di luar papan. Baris: 1-{n}, Kolom: A-{chr(ord('A')+n-1)}")
                continue
            break
        except (ValueError, IndexError):
            print("Input tidak valid. Coba lagi.")

    print(f"\nPosisi awal kuda: ({start_row + 1}, {chr(ord('A') + start_col)})")
    print(f"Mencari solusi untuk papan {n}×{n}...\n")

    # Inisialisasi papan: -1 = belum dikunjungi
    board = [[-1] * n for _ in range(n)]
    board[start_row][start_col] = 0  # Langkah pertama = 0

    # Panggil fungsi rekursif
    if solve_knights_tour(board, start_row, start_col, 1, n):
        print(f"Solusi ditemukan! Kuda berhasil mengunjungi semua {n*n} petak.\n")
        print("  Papan (angka = urutan kunjungan):")
        print_board(board, n)
        print_path(board, n)
    else:
        print("Tidak ada solusi yang ditemukan dari posisi awal ini.")
        print("Coba posisi awal yang berbeda.")

    print("Selesai!")


if __name__ == "__main__":
    main()
