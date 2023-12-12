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

def generer_cle_rsa(p, q, e):
    # Étape 1 : Calculer n = p * q
    n = p * q

    # Étape 2 : Calculer phi(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)

    # Étape 3 : Calculer d, l'inverse modulaire de e mod phi(n)
    d = mod_inverse(e, phi_n)

    # Clé publique : (e, n)
    cle_publique = (e, n)
    # Clé privée : (d, n)
    cle_privee = (d, n)

    return cle_publique, cle_privee

def chiffrement(message, cle_publique):
    e, n = cle_publique
    c = pow(message, e, n)
    return c

def dechiffrement(ciphertext, cle_privee):
    d, n = cle_privee
    m = pow(ciphertext, d, n)
    return m

# Saisie des paramètres par l'utilisateur
p = int(input("Entrez la valeur de p (nombre premier) : "))
q = int(input("Entrez la valeur de q (nombre premier différent de p) : "))
e = int(input("Entrez la valeur de e (entier premier avec (p-1)*(q-1)) : "))
m = int(input("Entrez la valeur du message m : "))
x = int(input("Entrez la valeur de la clé x pour le chiffrement : "))

# Génération des clés
cle_publique, cle_privee = generer_cle_rsa(p, q, e)

# Chiffrement
ciphertext = chiffrement(m + x, cle_publique)
print(f"Message chiffré : {ciphertext}")

# Déchiffrement
decrypted_message = dechiffrement(ciphertext, cle_privee)
print(f"Message déchiffré : {decrypted_message - x}")
print("Clé privée   :", cle_privee)