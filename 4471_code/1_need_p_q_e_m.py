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

# Calculer n et phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Clé publique : (e, n)
cle_publique = (e, n)

# Calculer d, l'inverse modulaire de e mod phi(n)
d = pow(e, -1, phi_n)

# Clé privée : (d, n)
cle_privee = (d, n)

# Chiffrement
ciphertext = chiffrement(m, cle_publique)
print(f"Message chiffré : {ciphertext}")
print("Clé privée   :", cle_privee)

# Déchiffrement
decrypted_message = dechiffrement(ciphertext, cle_privee)
print(f"Message déchiffré : {decrypted_message}")

# Vérification
if m == decrypted_message:
    print("Test réussi.")
else:
    print("Erreur dans le test.")