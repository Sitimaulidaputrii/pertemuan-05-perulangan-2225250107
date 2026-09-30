# Input: menerima nilai ujian 0 sampai 100.
# Proses: memeriksa apakah nilai berada pada rentang 0 sampai 100.
# Kondisi berhenti: perulangan berhenti ketika nilai sudah berada dalam rentang 0 sampai 100.
# Ouput: menampilkan pesan jika nilai tidak valid dan nilai yang diterima.

nilai = float(input("Nilai 0-100: "))
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))
print(f"Nilai diterima: {nilai}")    