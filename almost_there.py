def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

w = almost_there(90)
x = almost_there(104)
y = almost_there(150)
z = almost_there(209)

print(f"90: {w}")
print(f"104: {x}")
print(f"150: {y}")
print(f"209: {z}")
