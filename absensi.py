import csv 
import os
filename= "kedairan.csv"
def buat_file():
    if not os.path.exists(filename):
        with open(filename, "w",newline="") as f:
            buat = csv.writer(f)
            buat.writerow(["nama","pertemuan1","pertemuan2","pertemuan3"])

    
def absen(nama,per1,per2,per3):
    with open(filename, "a",newline="") as f:
        absen = csv.writer(f)
        absen.writerow([nama,per1,per2,per3])

def tampilkan_absen():
    with open(filename, "r") as f:
        baca = csv.reader(f)
        for baris in baca:
            print(baris)
