arr = []
for i in range(10):
    angka = int(input('Masukkan nilai: '))
    arr.append(angka)
print('Array            : ',arr)
print('======================================')
print('Nilai tertinggi  :', max(arr))
print("Nilai Terendah   :", min(arr))
print("Rata-Rata        :",sum(arr)/len(arr))
#hitung jumlah mahasiswa lulus
lulus = [n for n in arr if n>=60]
jumlah_lulus = len(lulus)
print("Jumlah Mahasiswa yang lulus: ", jumlah_lulus)

