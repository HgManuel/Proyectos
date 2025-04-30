x = ["manzana", "limon"]
y = ["banana", "limon"]
z = x 
print(x is z)
print(x is y)
print(x == y)

print("---------------------------")

x = ("manzana", "limon")
print("manzana" in x)

x = ("manzana", "limon")
print("pera" not in x)

print("---------------------------")

x = min(120, 200, 300)
y = max(5, 78, 305)
print(x)
print(y)

print("---------------------------")

x = abs(-300.5)
print(x)

x = pow(5,3)
print(x)

print("---------------------------")

import math
x = math.sqrt(25)
print(x)

print("---------------------------")

import math
x = math.ceil(2.6)
y = math.floor(2.6)
print(x)
print(y)

print("---------------------------")

import math
x = math.pi
print(x)

print("---------------------------")

print()