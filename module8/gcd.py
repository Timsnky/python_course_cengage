
def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while b > 0:
        print(a, b)
        a, b = b, a % b

    print(a)


gcd(15, 9)

