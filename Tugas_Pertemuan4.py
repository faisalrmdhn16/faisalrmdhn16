# NAMA   : FAISAL RAMADHAN
# NIM    : 12210342
# KELAS  : 12.1A.06

#input
print("         PROGRAM HITUNG GAJI KARYWAN")
n_k=(input("Nama Karyawan: "))
golJabatan=(input("Golongan Jabatan 1/2/3: "))
pendidikan=(input("Pendidikan SMA/D1/D3/S1: "))
jamkerja=int(input("Jumlah jam kerja: "))
gaji= 300000
#proses tunjangan jabatan
if golJabatan=="1":
    persentase="5%"
    tunjanganJab= 0.05 * gaji
elif golJabatan=="2":
    persentase="10%"
    tunjanganJab= 0.1 * gaji
elif golJabatan=="3":
    persentase="15%"
    tunjanganJab= 0.15 * gaji
else :
    print("input yang anda masukkan salah")
# proses tunjangan pendidikan
if pendidikan=="SMA" or "sma":
    persentase="2.5%"
    tunjpendidikan= 0.025 * gaji
elif pendidikan=="D1" or "d1":
    persentase="5%"
    tunjpendidikan= 0.05 * gaji
elif pendidikan=="D3" or "d3":
    persentase="20%"
    tunjpendidikan= 0.2 * gaji
elif pendidikan=="S1" or "s1":
    persentase="30%"
    tunjpendidikan= 0.3 * gaji
else: print("input yang anda masukkan salah")

# proses honor lembur
lembur = 3500
if jamkerja >8:
    honorlembur= (jamkerja-8) * lembur
else:
    honorlembur= 0
#total gaji
totalgaji= gaji + tunjpendidikan + tunjanganJab + honorlembur
#output
print("----------------------------------")
print("Karyawan yang bernama :", n_k)
print("Honor yang di terima ")
print("     Tunjangan Jabatan   :Rp.",tunjanganJab)
print("     Tunjangan Pendidikan:Rp.",tunjpendidikan)
print("     Honor Lembur        :Rp.", honorlembur)
print("                             ________________+")
print("Total Gaji               :   ",totalgaji)

