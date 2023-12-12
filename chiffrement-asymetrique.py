import random
from math import gcd

def exponentiaiton_rapide(base, exp, m):
    result = 1
    while(exp > 0):
        if( (exp & 1) > 0 ):
            result = (result * base) % m
        exp >>= 1
        base = (base * base) % m

    return result


def euclide(a, b):
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1

    while r2 != 0:
        q = r // r2
        r, u, v, r2, u2, v2 = (r2, u2, v2, r - q * r2, u - q * u2, v - q * v2)

    return r, u, v


def temoin_de_Miller(n, a):
    if n < 3 or n % 2 == 0 or a <= 1:
        raise ValueError("Les conditions d'entrée ne sont pas remplies.")

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return False

    for _ in range(s - 1):
        x = (x * x) % n

        if x == n - 1:
            return False

    return True


def miller_rabin(n, k):
    if n < 3 or n % 2 == 0 or k < 1:
        raise ValueError("Les conditions d'entrée ne sont pas remplies.")

    for _ in range(k):
        a = random.randint(2, n - 1)
        if temoin_de_Miller(n, a):
            return False

    return True
    
if __name__ == "__main__":
    result = exponentiaiton_rapide(4, 13, 497)
    resultat_euclide = euclide(120,23)
    resultat_test_miller = temoin_de_Miller(561,2)
    resultat_miller_rabin = miller_rabin(563,5)
    print("Exponentiation rapide: ",result)
    print("\n")
    print("Euclide: ", resultat_euclide)
    print("\n")
    print("Temoin de Miller: ", resultat_test_miller)
    print("\n")
    print("Le nombre {} est probablement premier : {}".format(563,resultat_miller_rabin))
    
    
