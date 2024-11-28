#### Imports et définition des variables globales
'''code pour l'exercice aasciiart'''

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    res = []
    c = s[0]
    n = 1
    for i in s[1:]:
        if i == c:
            n += 1
        else:
            res.append((c, n))
            c = i
            n = 1
    res.append((c, n))
    return res

def artcode_r(s):
    '''méthode secondaire récursive pour artcode'''
    if not s:
        return []
    c = s[0]
    n = 1
    while n < len(s) and s[n] == c:
        n += 1

    # appel récursif
    return [(c, n)] + artcode_r(s[n:])
#### Fonction principale


def main():
    '''main'''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
