### slope

input1 = input()
input2 = input()

input1 = input1.split()

input2 = input2.split()

y1, y2 = int(input2[1]), int(input1[1])

x1, x2 = int(input2[0]), int(input1[0])


hasil = (y1 - y2) // (x1 - x2)


print(round(hasil))

## network


# network
inputip = eval(input())

inputsub = eval(input())

pecah1,pecah2,pecah3,pecah4 = inputip

acah1,acah2,acah3,acah4 = inputsub

print(f"IP Address : ({pecah1}, {pecah2}, {pecah3}, {pecah4})")

print(f"Subnet Mask : ({acah1}, {acah2}, {acah3}, {acah4})")

print(f"Network Address : ({pecah1 & acah1}, {pecah2 & acah2}, {pecah3 & acah3}, {pecah4 & acah4})")

print(f"Broadcast Address : ({(pecah1 & acah1) | (255 - acah1)}, {(pecah2 & acah2) | (255 - acah2)}, {(pecah3 & acah3) | (255 - acah3)}, {(pecah4 & acah4) | (255 - acah4)})")

