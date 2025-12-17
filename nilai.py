import csv
import os
filename = "nilai_mahasiswa.csv"
TOTAL_PERTEMUAN = 16


def buat_file():
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            penulis = csv.writer(file)
            penulis.writerow([
            "Nama", "Tugas", "UTS", "UAS",
            "Nilai Akhir", "Grade",
            ])
        

    

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)


def konversi_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


def tambah_nilai(nama, tugas, uts, uas):
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    grade = konversi_grade(nilai_akhir)
    

    with open(filename, mode="a", newline="") as file:
        penulis = csv.writer(file)
        penulis.writerow([
            nama,
            tugas,
            uts,
            uas,
            round(nilai_akhir, 2),
            grade
        ])


def baca_data():
    with open(filename, mode="r") as file:
        pembaca = csv.reader(file)
        for baris in pembaca:
            print(baris)

        
