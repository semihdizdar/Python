# (Recursion) Özyineleme ile faktoriyel hesaplama

def faktoriyel(a):
    if a==1:
        return 1
    else:
        return a*faktoriyel(a-1)

print faktoriyel(5)
