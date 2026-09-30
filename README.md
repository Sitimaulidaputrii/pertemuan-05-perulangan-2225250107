# Pertemuan 5 Perulangan Python

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Memahami dan menerapkan penggunaan perulangan for dan while dalam Python untuk menjalankan proses secara berulang, melakukan validasi input, mengolah data pada setiap perulangan, penggunaan range, serta melakukan validasi input hingga mendapatkan hasil yang sesuai.

## Cara Menjalankan

Program dapat dijalankan melalui Terminal VS Code dengan perintah:

```bash
python kuis/kuis2_deret_aritmetika.py
```

Untuk menjalankan yang lainnya, sesuaikan nama folder dan file dengan program yang ingin dijalankan.

## Algoritma Kuis 2

1. Masukkan nilai suku pertama a.
2. Masukkan nilai beda d.
3. Masukkan banyak suku n.
4. Periksa nilai n. Jika n ≤ 0, maka masukkan kembali nilai n sampai nilainya positif.
5. Atur nilai total = 0.
6. Gunakan perulangan for untuk menghasilkan sebanyak n suku.
7. Hitung setiap suku dengan rumus suku = a + i × d.
8. Tampilkan setiap suku dan tambahkan nilainya ke total.
9. Setelah semua suku selesai dihitung, tampilkan jumlah seluruh suku.

## Hasil Pengujian

| Input(a, d, n) | Keluaran yang diharapkan | Keluaran aktual | Status |
| --- | --- | --- | --- |
| 2, 3, 5 | Suku: 2, 5, 8, 11, 14; Jumlah: 40 | Suku: 2.0, 5.0, 8.0, 11.0, 14.0; Jumlah: 40.00 | Berhasil |
| 10, -2, 4 | Suku: 10, 8, 6, 4; Jumlah: 28 | Suku: 10.0, 8.0, 6.0, 4.0; Jumlah: 28.00 | Berhasil |
| 1.5, 0.5, 3 | Suku: 1.5, 2.0, 2.5; Jumlah: 6.0 | Suku: 1.5, 2.0, 2.5; Jumlah: 6.00 | Berhasil |

## Refleksi

Pada latihan ini, saya memahami bahwa perulangan for digunakan untuk menghasilkan setiap suku sesuai dengan banyak suku yang diberikan. Saya juga memahami penggunaan while untuk memastikan nilai n yang dimasukkan sesuai dengan ketentuan sebelum proses perulangan.

Kesalahan yang saya temukan adalah menggunakan range (n-1) pada perulangan, sehingga jumlah suku yang ditampilkan kurang satu dari yang seharusnya. Kesalahan tersebut diperbaiki dengan menggunakan range (n) agar perulangan berjala sebanyak jumlah suku yang dimasukkan.

## Sumber 

Materi_Pertemuan_05_Perulangan Algoritma dan Pemrograman: Perulangan for dan while dalam Python di VS Code dan Pengumpulan melalui GitHub.