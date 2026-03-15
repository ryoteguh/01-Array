# Sistem Pengelolaan Nilai Mahasiswa Menggunakan Array

## Deskripsi Program

Program ini dibuat menggunakan bahasa Python untuk mensimulasikan pengelolaan data nilai mahasiswa dengan menggunakan struktur data array . Program menerima input 10 nilai mahasiswa, kemudian melakukan beberapa proses analisis seperti mencari nilai tertinggi, nilai terendah, menghitung rata-rata, menghitung jumlah mahasiswa yang lulus, serta menampilkan grafik sederhana.

## Penjelasan Konsep Array

Array adalah struktur data yang digunakan untuk menyimpan sekumpulan data dengan tipe yang sama dalam satu variabel, di mana setiap elemen memiliki indeks (atau nomor alamat) untuk diakses.

Contoh sederhana:

nilai = [100, 25, 77, 59, 67]

Setiap elemen dapat diakses menggunakan indeks:

nilai[0]   # hasil: 100
nilai[2]   # hasil: 77

Karakteristik array:

* Menyimpan data secara berurutan
* Memiliki indeks mulai dari 0
* Akses elemen cepat (O(1))
* Cocok untuk data dengan ukuran tetap atau terkontrol

Dalam program ini, array digunakan untuk menyimpan 10 nilai mahasiswa.


## Fitur Program

* Input 10 nilai mahasiswa
* Menampilkan nilai tertinggi
* Menampilkan nilai terendah
* Menghitung rata-rata nilai
* Menghitung jumlah mahasiswa lulus (nilai >= 60)
* Menampilkan grafik nilai tertinggi dan terendah
* Menampilkan grafik data kelulusan


## Screenshot Hasil Eksekusi

![hasil program](screenshot%20input%20nilai%20dan%20grafik1.png)

## Analisis Kompleksitas

### 1. Input Data Nilai

Input dilakukan sebanyak 10 kali menggunakan loop.

Kompleksitas:
O(n)

Karena program membaca seluruh data satu per satu.


### 2. Mencari Nilai Tertinggi

Menggunakan fungsi `max()`.

Kompleksitas:
O(n)

Karena semua elemen diperiksa.


### 3. Mencari Nilai Terendah

Menggunakan fungsi `min()`.

Kompleksitas:
O(n)

Karena seluruh elemen dibandingkan.


### 4. Menghitung Rata-rata

Menggunakan fungsi `sum()`.

Kompleksitas:
O(n)

Karena semua elemen dijumlahkan.


### 5. Menghitung Kelulusan

Menggunakan loop untuk mengecek nilai >= 60.

Kompleksitas:
O(n)

Karena setiap elemen diperiksa satu per satu.


### Kesimpulan Kompleksitas

Mayoritas operasi pada program ini memiliki kompleksitas linear O(n), karena seluruh data harus ditelusuri.


## Refleksi Pembelajaran

Dari tugas ini dipahami bahwa array sangat efektif untuk menyimpan kumpulan data yang terstruktur dan mudah diakses menggunakan indeks.

Selain itu, visualisasi grafik membantu memahami distribusi hasil data secara lebih jelas.

Tugas ini juga menunjukkan bahwa operasi sederhana pada array tetap memiliki analisis kompleksitas yang penting dipahami dalam struktur data.

## Bahasa Pemrograman

* Python

## Library

* matplotlib
