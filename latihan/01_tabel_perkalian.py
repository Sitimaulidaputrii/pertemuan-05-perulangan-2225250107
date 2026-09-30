# Input: menerima satu bilangan bulat n.
# Proses: mengalikan n dengan bilangan 1-10 menggunakan for.
# Kondisi berhenti: perulangan berhenti setelah i mencapai 10.
# Output: menampilkan hasil perkalian n x 1 sampai n x 10.

n = int(input("Bilangan: "))
for i in range (1, 11):
    print(f"{n} x {i} = {n * i}")