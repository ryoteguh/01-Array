import matplotlib.pyplot as plt
#INPUT 10 NILAI MAHASISWA
nilai = []
for i in range(10):
    n = int(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    nilai.append(n)
#PROSES DATA
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / len(nilai)
lulus = 0
tidak_lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1
    else:
        tidak_lulus += 1
#OUTPUT HASIL
print("\n=== HASIL ANALISIS NILAI ===")
print("Data nilai:", nilai)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Rata-rata:", rata_rata)
print("Jumlah lulus:", lulus)
print("Jumlah tidak lulus:", tidak_lulus)
#GRAFIK NILAI TERTINGGI & TERENDAH
plt.figure(figsize=(6,4))
plt.bar(["Tertinggi", "Terendah"], [nilai_tertinggi, nilai_terendah])
plt.title("Grafik Nilai Tertinggi dan Terendah")
plt.ylabel("Nilai")
plt.show()
#GRAFIK KELULUSAN
plt.figure(figsize=(6,4))
plt.bar(["Lulus", "Tidak Lulus"], [lulus, tidak_lulus])
plt.title("Grafik Kelulusan Mahasiswa")
plt.ylabel("Jumlah Mahasiswa")
plt.show()