"""
Ce module contient la fonction isprime qui vérifie si un nombre est premier
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne la valeur de vérité de la proposition : p est-il premier ?
    Args:
        p: un potentiel nombre premier
    Returns:
        True or False 
    """
    # votre code ici
    premier = True

    if p == 1:
        premier = False
        return premier

    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            premier = False
            return premier
    return premier
#### Fonction principale

def main():
    """
    Réalise les tests pour vérifier des nombres premiers
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()

    print(isprime(1))
    print(isprime(13))
    print(isprime(20))


if __name__ == "__main__":
    main()
