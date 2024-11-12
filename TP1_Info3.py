from random import random

# Exercice 1
# 2)
'''nom = input("Saisissez votre nom : ")
age = int(input("Saisissez votre age : "))'''


# Exercice 2
# 1)
def SommeCarres(n):
    somme = 0
    for i in range(n+1):
        somme += i**2
    return somme

# 2)
def EstPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

'''print(EstPalindrome("kayak"))
print(EstPalindrome("mot"))
print(EstPalindrome(""))
print(EstPalindrome("azertreza"))
print(EstPalindrome("jiozfeuizfeioei"))'''

# 3)
def occurences(x, tab):
    L = []
    for i in range(len(tab)):
        if L[i] == x:
            L.append(i)
    return L


# Exercice 3
# 1)
def EntierAleatoire(n):
    return int((n+1)*random())

'''print(EntierAleatoire(4))'''

# 2)
def EntierMystere(n):
    nb = EntierAleatoire(n)
    essai = int(input("Entrez un nombre : "))
    while essai != nb:
        if essai < nb :
            print("Plus grand")
        else:
            print("Plus petit")
        essai = int(input("Entrez un nouveau nombre : "))
    print("BRAVO ! Le nombre etait ", nb, "! ")

'''EntierMystere(5)'''


# Exercice 4
# 1)
def Add(A, B):
    S = [len(A)*[0] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            S[i][j] = A[i][j] + B[i][j]
    return S

'''print(Add([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))'''
# Complexite : O(n²)

# 2)
def Mult(A, B):
    S = [len(A)*[0] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                S[i][j] += (A[i][k])*(B[k][j])
    return S

'''print(Mult([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))'''

# 3)
def Puissance(A, n):
    if n == 0:
        S = [len(A)*[0] for i in range(len(A))]
        for i in range(len(A)):
            S[i][i] = 1
        return S
    if n == 1:
        return A
    if n%2 == 0:
        return Mult(Puissance(A, n/2), Puissance(A, n/2))
    else:
        return Mult(A, Mult(Puissance(A, int(n/2)), Puissance(A, int(n/2))))

print(Puissance([[1, 2], [3, 4]], 4))


# Exercice 5
# 1)
def EstPresent(x, tab):
    while 



























