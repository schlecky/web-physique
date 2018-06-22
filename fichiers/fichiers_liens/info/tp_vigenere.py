# TP Chiffre de Vigenere
import matplotlib.pyplot as plt

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def charNum(c):
    if c in alphabet:
        return ord(c)-ord('A')
    else :
        return 23 #X pour les caractères inconnus

# Question 1
def decalageDroite(car,cle):
    i = charNum(cle)
    return alphabet[(charNum(car)+charNum(cle))%26]


# Question 2
def decalageGauche(car,cle):
    i = charNum(cle)
    return alphabet[(charNum(car)-charNum(cle)+26)%26]

   
# Question 3
def chiffrer(texteClair,cle):
    texteChiffre=""
    iCle=0
    for c in texteClair:
        texteChiffre=texteChiffre+decalageDroite(c,cle[iCle])
        iCle=(iCle+1)%len(cle)
    return texteChiffre 
   
# Question 4  
def dechiffrer(texteChiffre,cle):
    texteClair=""
    iCle=0
    for c in texteChiffre:
        texteClair=texteClair+decalageGauche(c,cle[iCle])
        iCle=(iCle+1)%len(cle)
    return texteClair
   
# Question 5
def apparitions(texte):
    total=0
    occurences=[0]*26
    for c in texte:
        occurences[charNum(c)]+=1
    return occurences

#Question 6
def IC(texte):
    L = apparitions(texte)
    somme = 0
    n = 0
    for v in L:
        somme += v*(v-1)
        n+=v
    return somme/(n*(n-1))
    
#Question 7
def trouveLongueurCle(texte):
    Nmax=20
    for i in range(1,Nmax):
        x=0
        for j in range(i):
            x+= IC(texte[j::i])
        x=x/i
        if x>0.061:
            return i
    return -1
   
#Question 8
def frequences(texte):
    L=apparitions(texte)
    n=len(texte)
    for i in range(len(L)):
        L[i] = L[i]/n
    return L

#Question 9
def litFichier(nomFichier):
    fich=open(nomFichier,'r')
    texte=fich.read()
    return texte
    
freqRef = frequences(litFichier('miserables.txt'))

#Question 10
def decalage(F,i):
    L=[0]*26
    for j in range(26):
        L[j]=F[(i+j)%26]
    return L
    
#Question 11
def dist(F1,F2):
    d=0
    for i in range(len(F1)):
        d+=(F1[i]-F2[i])**2
    return d
    
#Question 12
def trouveDecalage(texte):
    freq = frequences(texte)
    d = 26
    s = 0
    for i in range(26):
        x = dist(freqRef,decalage(freq,i))
        if x<d:
            d=x
            s=i
    return s

#Question 13
def trouveCle(texteChiffre):
    lCle = trouveLongueurCle(texteChiffre)
    cle=""
    for i in range(lCle):
        x=trouveDecalage(texteChiffre[i::lCle])
        cle = cle+alphabet[x]
    return cle
   
