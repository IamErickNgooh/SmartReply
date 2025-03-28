tab = [x * x for x in range(1, 11)]
print(tab)
print("\n")

paire = [x for x in range(1, 22) if x % 2 == 0]
print(paire)
print("\n")

res = ["pair" if x % 2 == 0 else 'impair' for x in range(1, 11)]
print(res)
print("\n")

cube = (pow(x, 3) for x in range(0, 11))
for i in range(0, 11):
    print(f"{i} -- {next(cube)}")
print("\n")

res = (x for x in range(0, 11))
for i in range(0, 11):
    print(f"{i} -- {next(res)}")
print("\n")

sum = sum((x for x in range(1, 1001) if x % 3 == 0))
print(sum)
print("\n")

seven =  any((x for x in range(1, 101) if x % 7 == 0))
print(seven)
print("\n")

positif = all(True if x > 0 else False for x in range(1, 1001))
print(positif)
print("\n")

negatif = all(True if x < 0 else False for x in range(1, 1001))
print(negatif)
print("\n")

test = [x for x in range(0, 11)]
print(test)
print(type(test))
print("\n")

test = (x for x in range(0, 11))
print(test)
print(type(test))
print("\n")

cartesien = [(x, y) for x in [1, 2] for y in [10, 20, 30]]
print(cartesien)
print("\n")

liste = [[1, 2], [3, 4], [5]]
res = [y for x in liste for y in x]
print(res)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

from itertools import chain

liste = [[1, 2], [3, 4], [5]]
res = list(chain.from_iterable(liste))
print(res)
print("\n")