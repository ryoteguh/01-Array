def sistem_nilai_mahasiswa():
    #definisi array kosong untuk input nilai
    nilai = []
    for i in range(10):
        angka = int(input(f'Masukkan nilai ke-{i+1}: '))
        nilai.append(angka)
    #proses nilai
    tertinggi = max(nilai)
    terendah = min(nilai)
    rata_rata = sum(nilai)/len(nilai)
    lulus = [n for n in nilai if n >=60]
    jumlah_lulus = len(lulus)
    #menampilkan informasi dari hasil proses
    print('Nilai dalam Array            : ',nilai)
    print('======================================')
    print('Nilai tertinggi  :', tertinggi)
    print("Nilai Terendah   :", terendah)
    print("Rata-Rata        :", rata_rata)
    print("Jumlah Mahasiswa yang lulus: ", jumlah_lulus)
sistem_nilai_mahasiswa()

