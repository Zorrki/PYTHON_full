# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8
a=3
b=5
print(a)
print(b)
def step(a, b):
    if b == 0:
        return 1
    else:
        return a * step(a, b - 1)

print(step(2, 3))