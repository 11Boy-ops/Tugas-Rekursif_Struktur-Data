"""
=============================================================
  SOAL 3: KNAPSACK PROBLEM (MASALAH KARUNG/TAS)
  Algoritma: Rekursif dengan Backtracking
=============================================================
  Tujuan: Menemukan kombinasi barang yang totalnya TEPAT
  sama dengan berat target (atau <= target jika tidak ada
  yang tepat).
  
  Pendekatan: Untuk setiap barang, kita punya 2 pilihan:
  1. MASUKKAN ke knapsack (jika berat masih mencukupi)
  2. LEWATI barang ini
  Rekursi terus sampai target tercapai atau semua barang dicoba.
=============================================================
"""


def knapsack_recursive(items, index, remaining_weight, current_items, all_solutions, find_all=False):
    """
    Fungsi rekursif untuk menyelesaikan Knapsack Problem.
    
    Parameter:
    - items          : daftar berat semua barang
    - index          : indeks barang yang sedang dipertimbangkan
    - remaining_weight: sisa kapasitas knapsack
    - current_items  : daftar barang yang sudah dimasukkan
    - all_solutions  : daftar semua solusi yang ditemukan
    - find_all       : True = cari semua solusi, False = cari satu solusi
    
    Base case 1 : remaining_weight == 0 → berat target tercapai
    Base case 2 : index >= len(items)   → semua barang sudah dicoba
    Rekursi     : coba masukkan barang index, lalu rekursi ke index+1
                  ATAU lewati barang index, lalu rekursi ke index+1
    """
    # BASE CASE 1: Berat target tepat tercapai → simpan solusi
    if remaining_weight == 0:
        all_solutions.append(current_items[:])  # Simpan salinan
        return True  # Solusi ditemukan

    # BASE CASE 2: Semua barang sudah dicoba atau sisa berat negatif
    if index >= len(items) or remaining_weight < 0:
        return False

    found = False

    # PILIHAN 1: MASUKKAN barang ke-index
    if items[index] <= remaining_weight:
        current_items.append(items[index])                          # Masukkan barang
        result = knapsack_recursive(
            items, index + 1,
            remaining_weight - items[index],                        # Kurangi sisa berat
            current_items, all_solutions, find_all
        )
        if result:
            found = True
        current_items.pop()                                          # Backtrack: keluarkan barang

    # Jika sudah menemukan solusi dan tidak perlu cari semua, berhenti
    if found and not find_all:
        return True

    # PILIHAN 2: LEWATI barang ke-index
    result = knapsack_recursive(
        items, index + 1,
        remaining_weight,                                            # Sisa berat tidak berubah
        current_items, all_solutions, find_all
    )
    if result:
        found = True

    return found


def knapsack_best_fit(items, target_weight):
    """
    Mencari kombinasi terbaik jika tidak ada solusi tepat.
    Menggunakan rekursi untuk menemukan kombinasi dengan total
    sebesar mungkin tapi tidak melebihi target.
    """
    best = [0, []]  # [total_berat_terbaik, kombinasi_terbaik]

    def helper(index, remaining, current, current_total):
        # Update solusi terbaik
        if current_total > best[0]:
            best[0] = current_total
            best[1] = current[:]

        if index >= len(items) or remaining <= 0:
            return

        # Masukkan barang
        if items[index] <= remaining:
            current.append(items[index])
            helper(index + 1, remaining - items[index],
                   current, current_total + items[index])
            current.pop()

        # Lewati barang
        helper(index + 1, remaining, current, current_total)

    helper(0, target_weight, [], 0)
    return best[0], best[1]


def get_items_input():
    """Meminta input daftar barang dari pengguna."""
    print("\nCara memasukkan barang:")
    print("  a) Masukkan manual")
    print("  b) Gunakan contoh dari soal (2, 5, 6, 9, 12, 14, 20)")

    choice = input("Pilihan (a/b): ").strip().lower()

    if choice == 'b':
        items = [2, 5, 6, 9, 12, 14, 20]
        print(f"Menggunakan contoh: {items}")
        return items

    print("Masukkan berat barang dipisahkan spasi (contoh: 2 5 6 9 12):")
    while True:
        try:
            items = list(map(int, input("Berat barang: ").split()))
            if not items:
                print("Minimal satu barang. Coba lagi.")
                continue
            if any(w <= 0 for w in items):
                print("Berat harus positif. Coba lagi.")
                continue
            return items
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat positif dipisah spasi.")


def main():
    print("=" * 55)
    print("       PROGRAM KNAPSACK (MASALAH KARUNG)")
    print("=" * 55)
    print("Tujuan: Menemukan kombinasi barang yang totalnya")
    print("sama dengan berat target menggunakan rekursi.\n")

    # Input barang
    items = get_items_input()

    # Input berat target
    while True:
        try:
            target = int(input("\nMasukkan berat target knapsack: "))
            if target <= 0:
                print("Berat target harus positif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid.")

    # Pilih mode pencarian
    print("\nMode pencarian:")
    print("  1. Cari SATU solusi (cepat)")
    print("  2. Cari SEMUA solusi (mungkin lambat untuk banyak barang)")
    mode = input("Pilihan (1/2): ").strip()
    find_all = (mode == '2')

    # Info input
    print(f"\n{'=' * 45}")
    print(f"Daftar barang : {sorted(items)}")
    print(f"Jumlah barang : {len(items)}")
    print(f"Berat target  : {target}")
    print(f"Mode          : {'Cari semua solusi' if find_all else 'Cari satu solusi'}")
    print(f"{'=' * 45}")
    print("Mencari solusi...\n")

    # Urutkan barang (optimasi ringan)
    items_sorted = sorted(items)
    solutions = []

    # Panggil fungsi rekursif
    knapsack_recursive(items_sorted, 0, target, [], solutions, find_all)

    if solutions:
        print(f"✓ SOLUSI DITEMUKAN! ({len(solutions)} kombinasi)\n")

        # Tampilkan maksimal 10 solusi
        show = min(10, len(solutions))
        for i, sol in enumerate(solutions[:show]):
            total = sum(sol)
            print(f"  Solusi #{i+1}: {sol}")
            print(f"            Total berat = {total} (target = {target})")
            leftovers = items_sorted[:]
            for item in sol:
                leftovers.remove(item)
            print(f"            Barang tidak masuk: {leftovers}")
            print()

        if len(solutions) > 10:
            print(f"  ... dan {len(solutions) - 10} solusi lainnya.\n")
    else:
        print("✗ Tidak ada kombinasi yang TEPAT mencapai berat target.\n")
        print("Mencari kombinasi terbaik (mendekati target)...")
        best_total, best_combo = knapsack_best_fit(items_sorted, target)
        if best_combo:
            print(f"\n  Kombinasi terbaik: {best_combo}")
            print(f"  Total berat      : {best_total} dari target {target}")
            print(f"  Selisih          : {target - best_total}")
        else:
            print("  Tidak ada barang yang bisa dimasukkan.")

    print("\nSelesai!")


if __name__ == "__main__":
    main()
