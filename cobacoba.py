
a = eval(input())
anyar = dict()

if a and all(isinstance(item, tuple) for item in a):

    for nama, jumlah, harga_satuan in a:
        total = jumlah * harga_satuan
        if nama in anyar:
            anyar[nama] += total
        else:
            anyar[nama] = total

    hasil = tuple(sorted(anyar.items(), key=lambda x: x[1], reverse=True))
    print(f"Hasil Prof : {hasil}")

else:
    print("Hasil Prof : Gak Niat Belanja Ta?")

====================================
import math
a = input().split()
b = input().split()
x1, y1 = int(a[0]), int(a[1])
x2, y2 = int(b[0]), int(b[1])
jarak = math.hypot(x2 - x1, y2 - y1)
print(round(jarak))
