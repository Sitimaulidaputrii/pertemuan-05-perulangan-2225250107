# Input: menerima satu bilangan n positif 
# Proses: memeriksa bilangan dari 1 sampai n dan menghitung bilangan genap.
# Kondisi berhenti: perulangan berhenti setelah i mencapai n.
# Output: menampilkan banyak bilangan genap dari 1 sampai n.

n = int(input("n: "))
jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1
print(f"Banyak bilangan genap = {jumlah_genap}")        