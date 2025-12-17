import data_mahasiswa as siswa
import nilai as n
import absensi as a

class mahasiswa:
    def __init__(self):
        self.menu = [
            "Tambah Siswa",
            "Input Nilai",
            "Input Presensi",
            "Tampilkan Data",
        ]
    def tampilkan_menu(self):
        print("----Manajemen Data Mahasiswa----")
        for i, menu in enumerate(self.menu, start=1):
            print(f"{i}.{menu}")
    def mulai_crud(self):
        print("--- Hallo Welcome---")
        siswa.buat_file()
        a.buat_file()
        n.buat_file()
        while True:
            self.tampilkan_menu()
            user = input("masukan nilai (1-4)/ selesai = ")
            if user == "selesai":
                print("program selesai")
                break
            if user == "1":
                nama = input("masukan nama mahasiswa = ")
                nim = int(input("masukan nim = "))
                siswa.tambah_siswa(nama,nim)
            elif user == "2":
                nama = input("masukan nama siswa = ")
                tugas = int(input(f"masukan nilai tugas {nama} = "))
                uts = int(input(f"masukan nilai uts {nama} = "))
                uas = int(input(f"masukan nilai uas {nama} = "))
                n.tambah_nilai(nama,tugas,uts,uas)
            elif user == "3":
                nama = input("masukan nama siswa = ")
                p1 = input("masukan keterangan pertemuan ke 1 = ")
                p2 = input("masukan keterangan pertemuan ke 1 = ")
                p3 = input("masukan keterangan pertemuan ke 1 = ")
                a.absen(nama,p1,p2,p3)
            elif user == "4":
                siswa.baca_data()
                a.tampilkan_absen()
                n.baca_data()



                


ma = mahasiswa()
ma.mulai_crud()
