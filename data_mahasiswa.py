import csv
import os
filename = "data_mahasiswa.csv"

def buat_file():
    if not os.path.exists(filename):
        with open(filename, mode="w",newline="")as file:
            penulis = csv.writer(file)
            penulis.writerow(["nama","nim"])
    
        
def tambah_siswa(nama,nim):
    with open(filename,mode="a",newline="") as file:
        tambah = csv.writer(file)
        tambah.writerow([nama,nim])

def baca_data():
    with open(filename,mode ="r")as files:
        pembaca = csv.reader(files)
        for baris in pembaca:
            print(baris)