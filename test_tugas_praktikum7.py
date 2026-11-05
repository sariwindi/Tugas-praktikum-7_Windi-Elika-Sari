"""Unit test stdlib untuk tugas praktikum windi 7 (Soal 1-4).

Jalankan: python3 -m unittest test_tugas_praktikum7.py -v
Modul aman diimpor karena eksekusi hanya di bawah __main__.
"""
import importlib.util
import unittest

spec = importlib.util.spec_from_file_location(
    "tugas7", "tugas praktikum windi 7.py"
)
tugas7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tugas7)


class TestSoal1(unittest.TestCase):
    def test_hasil_akhir(self):
        self.assertEqual(
            tugas7.soal1_manipulasi_list(),
            ["motor", "becak", "mobil", "skuter", "bus"],
        )


class TestSoal2(unittest.TestCase):
    def test_terurut_terbesar_ke_terkecil(self):
        self.assertEqual(
            tugas7.soal2_operasi_nilai(),
            [100, 90, 85, 80, 75, 75, 65],
        )


class TestSoal3(unittest.TestCase):
    def test_gabung(self):
        self.assertEqual(
            tugas7.soal3_gabung_menu(),
            ["Nasi Goreng", "Mie Ayam", "Kerupuk", "Es Teh"],
        )


class TestSoal4(unittest.TestCase):
    def test_data_tetap(self):
        self.assertEqual(
            tugas7.soal4_nested_list(),
            [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]],
        )


if __name__ == "__main__":
    unittest.main()
