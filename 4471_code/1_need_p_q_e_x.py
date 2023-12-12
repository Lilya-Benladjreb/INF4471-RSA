def mod_inverse(a, m):
    # Calculer l'inverse modulaire de a modulo m
    g, x, _ = euclide_etendu(a, m)
    print("euclide_etendu", g,x)
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

# Saisie des paramètres par l'utilisateur
p = int(input("Entrez la valeur de p (nombre premier) : "))
q = int(input("Entrez la valeur de q (nombre premier différent de p) : "))
e = int(input("Entrez la valeur de e (entier premier avec (p-1)*(q-1)) : "))
x = int(input("Entrez la valeur du message chiffré x : "))

# Calcul des autres paramètres
n = p * q
phi_n = (p - 1) * (q - 1)

# Calcul de la clé de déchiffrement d
d = mod_inverse(e, phi_n)

# Déchiffrement du message x
clair = pow(x, d, n)

# Affichage des résultats
print("Clé de déchiffrement d :", d)
print("Message déchiffré(clair) :", clair)