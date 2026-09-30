# Input: menerima satu bilangan bulat positif n.
# Proses: menjumlahkan bilangan dari 1 sampai n menggunakan for.
# Kondisi berhenti: perulangan berhenti setelah i mencapai n.
# Output: menampilkan hasil jumlah bilangan dari 1 sampai n.

n = int(input("n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Jumlah: {total}")    