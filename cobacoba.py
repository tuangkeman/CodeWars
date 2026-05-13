### slope

input1 = input()
input2 = input()

input1 = input1.split()

input2 = input2.split()

y1, y2 = int(input2[1]), int(input1[1])

x1, x2 = int(input2[0]), int(input1[0])


hasil = (y1 - y2) // (x1 - x2)


print(round(hasil))
