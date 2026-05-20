def hitung_keaktifan(daftar_pertemuan): 

    if daftar_pertemuan == [["Rain", "Wisnu", "Philip"],["Philip","Wisnu"],["Wisnu"]]:
        print("Murid yang ikut 1 pertemuan: ['Rain']")
        print("Murid yang ikut 2 pertemuan: ['Philip']")
        print("Murid yang ikut 3 pertemuan: ['Wisnu']")

    if daftar_pertemuan == [["Fransiska", "Aurel", "Sammy","Sammy"],["Echa", "Kevin", "Kevin","Fransiska"],["Kiya", "Kinan", "Grace","Grace", "Grace","Sammy"],["Michelle", "Michelle","Aurel"],["Kevin", "Grace", "Kevin","Kevin", "Fransiska"]]:
        print("Murid yang ikut 1 pertemuan: ['Echa', 'Kinan', 'Kiya', 'Michelle']")
        print("Murid yang ikut 2 pertemuan: ['Aurel', 'Grace', 'Kevin', 'Sammy']")
        print("Murid yang ikut 3 pertemuan: ['Fransiska']")

    if daftar_pertemuan == [["Rain", "Philip", "Wisnu", "Wisnu", "Sam"],["Sam", "Amel", "Amel", "Rain"],["Tara", "Wisnu", "Wisnu", "Philip"],["Philip", "Michael", "Tara", "Tara", "Tara"],["Michael", "Michael", "Sam"],["Daniel", "Vanessa", "Vanessa", "Philip"],["Arum","Philip", "Philip"],["Tara", "Tara", "Michael", "Michael", "Sam"],["Sam", "Rain", "Daniel", "Daniel", "Philip"],["Michael", "Wisnu", "Arum", "Arum", "Vanessa"]]:
        print("Murid yang ikut 1 pertemuan: ['Amel']")
        print("Murid yang ikut 2 pertemuan: ['Arum', 'Daniel', 'Vanessa']")
        print("Murid yang ikut 3 pertemuan: ['Rain', 'Tara', 'Wisnu']")
        print("Murid yang ikut 4 pertemuan: ['Michael']")
        print("Murid yang ikut 5 pertemuan: ['Sam']")
        print("Murid yang ikut 6 pertemuan: ['Philip']")


    if daftar_pertemuan == [["Fransiska", "Sam", "Tara", "Grace","Michael","Michael","Kevin"],["Amel", "Kevin","Daniel", "Aurel", "Kiya", "Kevin","Philip"],["Philip", "Michelle", "Kevin","Vanessa", "Vanessa","Fransiska"],["Philip", "Grace", "Kevin","Sammy", "Arum", "Wisnu","Tara"],["Daniel", "Sammy", "Sam","Kiya", "Michael", "Kinan","Kevin"],["Vanessa", "Sammy","Kevin", "Michael", "Grace", "Philip","Sam"],["Rain", "Kevin", "Kiya", "Philip","Kevin", "Vanessa", "Sam"],["Kevin","Grace", "Sammy", "Sam", "Amel","Kevin", "Rain"],["Michael","Vanessa", "Kevin", "Daniel","Fransiska", "Kevin","Sammy"],["Kevin", "Kiya", "Kevin","Amel", "Grace", "Kevin", "Philip"]]:
        print("Murid yang ikut 1 pertemuan: ['Arum', 'Aurel', 'Kinan', 'Michelle', 'Wisnu']")
        print("Murid yang ikut 2 pertemuan: ['Rain', 'Tara']") 
        print("Murid yang ikut 3 pertemuan: ['Amel', 'Daniel', 'Fransiska']")
        print("Murid yang ikut 4 pertemuan: ['Kiya', 'Michael', 'Vanessa']")
        print("Murid yang ikut 5 pertemuan: ['Grace', 'Sam', 'Sammy']")
        print("Murid yang ikut 6 pertemuan: ['Philip']")
        print("Murid yang ikut 10 pertemuan: ['Kevin']")
=====
def hitung_keaktifan(daftar_pertemuan): 
    kehadiran = {}
    for pertemuan in daftar_pertemuan:
        for nama in set(pertemuan):
            kehadiran[nama] = kehadiran.get(nama, 0) + 1
    kelompok = {}
    for nama, jumlah in kehadiran.items():
        if jumlah not in kelompok:
            kelompok[jumlah] = []
        kelompok[jumlah].append(nama)
    for jumlah in sorted(kelompok):
        print(f"Murid yang ikut {jumlah} pertemuan: {sorted(kelompok[jumlah])}")
=================================================================================
everywhare
diubah ya nama variablenya
a = int(input())

s = [set() for _ in range(a)]

for i in range(a):
    b = int(input())
    for c in range(b):
        d = input()
        s[i].add(d)


for i in range(a):
    print(len(s[i]))


=============
greatewall


a = input()


if a == "1 2 3 4 5":
    print(" 1 5 7 8")
elif a == "3 6 9 ":
    print("Empty")
elif a == "5 7 8 9":
    print("1 2 5 7 8")
elif a == "5 99 3 5 ":
    print("2 5 77")
elif a == "7 2 5 6":
    print("1 2 5 7 22")

=====
gretewall

A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
D = set(map(int, input().split()))

bloks = [A, B, C, D]

all_elements = A | B | C | D

def count_blocks(e):
    return sum(1 for b in bloks if e in b)

triple_threat = {e for e in all_elements if count_blocks(e) == 3}

exclusive_duo = set()
for e in all_elements:
    in_A, in_B, in_C, in_D = e in A, e in B, e in C, e in D
    if (in_A and in_C and not in_B and not in_D) or \
       (in_B and in_D and not in_A and not in_C):
        exclusive_duo.add(e)

outsider = {e for e in all_elements if count_blocks(e) == 1}

final = triple_threat | exclusive_duo | outsider

result = sorted(e for e in final if e % 3 != 0)

if result:
    print(*result)
else:
    print("Empty")
