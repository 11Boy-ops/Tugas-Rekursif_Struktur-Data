"""
=============================================================
  SOAL 1: N-QUEENS (N-RATU)
  Algoritma: Backtracking Rekursif
=============================================================
  Tujuan: Menempatkan N ratu di papan N×N sehingga tidak ada
  dua ratu yang saling menyerang (baris, kolom, diagonal).
=============================================================
"""

def is_safe(board, row, col, n):
    """
    Memeriksa apakah aman menempatkan ratu di posisi (row, col).
    Cek kolom yang sama, diagonal kiri atas, dan diagonal kanan atas.
    """
    # Cek kolom yang sama di baris sebelumnya
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Cek diagonal kiri atas
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Cek diagonal kanan atas
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n, solutions):
    """
    Fungsi rekursif untuk menyelesaikan N-Queens.
    Mencoba menempatkan ratu satu per satu di setiap baris.
    
    Base case : row == n → semua ratu sudah ditempatkan (solusi ditemukan)
    Rekursi   : coba setiap kolom di baris saat ini, jika aman → lanjut ke baris berikutnya
    """
    # BASE CASE: semua ratu sudah ditempatkan
    if row == n:
        # Simpan salinan papan sebagai solusi
        solutions.append([r[:] for r in board])
        return

    # REKURSI: coba setiap kolom di baris saat ini
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'           # Tempatkan ratu
            solve_n_queens(board, row + 1, n, solutions)  # Rekursi ke baris berikutnya
            board[row][col] = '.'           # Backtrack: hapus ratu


def print_board(board, solution_num):
    """Mencetak papan catur dengan ratu."""
    n = len(board)
    print(f"\n  Solusi #{solution_num}:")
    print("  +" + "---+" * n)
    for i, row in enumerate(board):
        print("  |", end="")
        for cell in row:
            if cell == 'Q':
                print(" Q |", end="")
            else:
                print("   |", end="")
        print(f"  ← baris {i + 1}")
        print("  +" + "---+" * n)


def main():
    print("=" * 50)
    print("       PROGRAM N-QUEENS (N-RATU)")
    print("=" * 50)
    print("Tujuan: Menempatkan N ratu di papan N×N")
    print("sehingga tidak ada dua ratu yang saling menyerang.\n")

    while True:
        try:
            n = int(input("Masukkan ukuran papan (N): "))
            if n < 1:
                print("Ukuran papan harus minimal 1. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat positif.")

    # Inisialisasi papan kosong
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    print(f"\nMencari solusi untuk papan {n}×{n}...")

    # Panggil fungsi rekursif
    solve_n_queens(board, 0, n, solutions)

    if not solutions:
        print(f"\nTidak ada solusi untuk papan {n}×{n}.")
    else:
        print(f"\nDitemukan {len(solutions)} solusi!")

        # Tampilkan maksimal 3 solusi pertama agar tidak terlalu panjang
        show_count = min(3, len(solutions))
        print(f"Menampilkan {show_count} solusi pertama:\n")

        for i in range(show_count):
            print_board(solutions[i], i + 1)
            # Tampilkan posisi kolom setiap ratu
            positions = [solutions[i][row].index('Q') + 1 for row in range(n)]
            print(f"  Posisi ratu (per baris): {positions}\n")

        if len(solutions) > 3:
            print(f"  ... dan {len(solutions) - 3} solusi lainnya.")

    print("\nSelesai!")


if __name__ == "__main__":
    main()
