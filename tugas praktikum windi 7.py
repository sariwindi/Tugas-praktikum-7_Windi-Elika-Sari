"""Tugas Praktikum 7 - Manipulasi List (Soal 1-4).

Hasil keluaran sama seperti versi awal, tetapi tiap soal dibungkus
fungsi, tidak mengandalkan indeks hardcoded, dan aman diimpor
(tidak ada kode yang jalan saat import; lihat test_tugas_praktikum7.py).
"""


def soal1_manipulasi_list():
    kendaraan = ["motor", "mobil", "sepeda", "bus"]

    # a. Tambahkan "truk" di akhir list
    kendaraan.append("truk")
    print(kendaraan)

    # b. Sisipkan "becak" pada index ke-1
    kendaraan.insert(1, "becak")
    print(kendaraan)

    # c. Hapus data yang berada paling belakang dari list tersebut
    kendaraan.pop()
    print(kendaraan)

    # d. Ubah elemen "sepeda" menjadi "skuter"
    # Cari posisinya dulu; indeks hardcoded (3) rapuh kalau proses
    # insert di atas berubah.
    if "sepeda" in kendaraan:
        kendaraan[kendaraan.index("sepeda")] = "skuter"
    else:
        print("Elemen 'sepeda' tidak ditemukan, tidak ada yang diubah.")
    print(kendaraan)

    # e. Tampilkan informasi jumlah total data di dalam list tersebut
    panjang_kendaraan = len(kendaraan)
    print(f"Jumlah total data : {panjang_kendaraan}")
    return kendaraan


def soal2_operasi_nilai():
    angka = [75, 80, 90, 75, 85, 100, 65]

    # a. Cari tahu di indeks ke berapa skor 100 berada
    # list.index() melempar ValueError kalau 100 tidak ada.
    try:
        index_100 = angka.index(100)
        print(f"Angka 100 berada di index ke: {index_100}")
    except ValueError:
        print("Angka 100 tidak ditemukan dalam list.")

    # b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
    jumlah_75 = angka.count(75)
    print(f"Banyak siswa yang mendapatkan skor 75: {jumlah_75}")

    # c. Urutkan list dari nilai terkecil hingga terbesar
    print(f"Data sebelum diurutkan: \n{angka}")
    angka.sort()
    print(f"Data setelah diurutkan dari yang terkecil: \n{angka}")

    # d. Balikan urutan list yang sudah diurutkan (terbesar ke terkecil)
    angka.reverse()
    print(f"Data setelah diurutkan dari yang terbesar:\n{angka}")
    return angka


def soal3_gabung_menu():
    menu_utama = ["Nasi Goreng", "Mie Ayam"]
    menu_tambahan = ["Kerupuk", "Es Teh"]
    print(f"List sebelum digabungkan \n{menu_utama} dan {menu_tambahan}")
    menu_utama.extend(menu_tambahan)
    print(f"List setelah digabungkan \n{menu_utama}")
    return menu_utama


def soal4_nested_list():
    # [[nama barang, harga], ...]
    data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

    # a. Tampilkan harga dari "Pensil"
    # Cari berdasarkan nama, bukan indeks baris hardcoded [1][1].
    pensil = next((harga for nama, harga in data_barang if nama == "Pensil"), None)
    if pensil is None:
        print("Barang 'Pensil' tidak ditemukan.")
    else:
        print(f"nama barang dan harga: Pensil {pensil}")

    # b. Perulangan untuk menampilkan nama dan harga tiap barang
    for i, barang in enumerate(data_barang):
        if not isinstance(barang, list) or len(barang) != 2:
            print(f"Data ke-{i + 1} tidak valid, dilewati: {barang}")
            continue
        print(f"Nama barang\t: {barang[0]}")
        print(f"Harga barang\t: {barang[1]}")
    return data_barang


def main():
    soal1_manipulasi_list()
    soal2_operasi_nilai()
    soal3_gabung_menu()
    soal4_nested_list()


if __name__ == "__main__":
    main()
