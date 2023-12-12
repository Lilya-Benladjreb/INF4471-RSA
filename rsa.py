import random
from math import gcd

def generer_premier():
    # Génère un nombre premier aléatoire
    while True:
        nombre = random.randint(1000, 10000)
        if est_premier(nombre):
            return nombre

def est_premier(nombre):
    # Vérifie si un nombre est premier
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def generer_cle_rsa():
    # Étape 1 : Générer deux grands nombres premiers, p et q
    p = generer_premier()
    q = generer_premier()

    # Étape 2 : Calculer n = p * q
    n = p * q

    # Étape 3 : Calculer phi(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)

    # Étape 4 : Générer un nombre e tel que PGCD(e, phi(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Étape 5 : Calculer d, l'inverse modulaire de e mod phi(n)
    d = mod_inverse(e, phi_n)

    # Clé publique : (e, n)
    cle_publique = (e, n)
    # Clé privée : (d, n)
    cle_privee = (d, n)

    return cle_publique, cle_privee, p, q

def mod_inverse(a, m):
    # Calculer l'inverse modulaire de a modulo m
    g, x, _ = euclide_etendu(a, m)
    if g != 1:
        raise ValueError("L'inverse modulaire n'existe pas.")
    else:
        return x % m

def euclide_etendu(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = euclide_etendu(b % a, a)
        return g, y - (b // a) * x, x

def chiffrement(message, cle_publique):
    e, n = cle_publique
    c = pow(message, e, n)
    return c

def dechiffrement(ciphertext, cle_privee):
    d, n = cle_privee
    m = pow(ciphertext, d, n)
    return m

# Génération des clés
cle_publique, cle_privee, p, q = generer_cle_rsa()

# Affichage des clés
print("Clé publique :", cle_publique)
print("Clé privée   :", cle_privee)
print("p            :", p)
print("q            :", q)

# Validation
message = random.randint(1, 1000)

# Chiffrement
ciphertext = chiffrement(message, cle_publique)

# Déchiffrement
decrypted_message = dechiffrement(ciphertext, cle_privee)

# Vérification
if message == decrypted_message:
    print("Test réussi.")
else:
    print("Erreur dans le test.")

