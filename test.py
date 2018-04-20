#import nltk
import re
a = open("ctest.txt","r")
corpus=a.readlines()       #le corpus en liste

corpuss=str(corpus)        #le corpus en une seule chaîne


def before(mot, corpus):
    a=corpus.split(mot)
    return(a[0])

def after(mot, corpus):
    a=corpus.split(mot)
    return(a[1])




i=0
s=0
liste=[]    #Liste des ID des phrases contenant une personne dont le nom commence par E
liste2=[]   #Liste du contenu des phrases avec les ID en question
liste3=[]   #Liste du contenu des phrases ayant également un mot présent dans le champs lexical du meutre
lpresent=0

lemme=["assassinate","drown","execute","massacre","murder","poison","slaughter","slay","annihilate","asphyxiate","crucify","electrocute","finish","garrote","guillotine","immolate","liquidate","lynch","neutralize","smother","strangle","suffocate"]

for i in range(len(corpus)):                    #Voir commentaire liste
    if corpus[i].find("<sentence id=")!=-1:     #Stockage de l'ID de la phrase quand trouvée
        s=before('"',after('"',corpus[i]))      #Récupération de l'ID dans la ligne
    if corpus[i].find(">PERSON<")!=-1:
        if corpus[i-5].find("<word>E")!=-1:
            liste.append(s)

i=0
for i in range(len(liste)):                     #Voir commentaire liste2
    if corpuss.find('<sentence id="'+str(liste[i])+'"')!=-1:           #Nécessaire pour éviter out of range si absence du mot
        corpuss=after('<sentence id="'+str(liste[i])+'"',corpuss)      #Elagation du contenu déjà exploré du "corpuss"
    liste2.append(before('</sentence>',corpuss))

i=0
    
for i in range(len(liste2)):                    #Voir commentaire liste3
    for j in range(len(lemme)):
        if liste2[i].find(lemme[j])!=-1:
            lpresent=1
    if lpresent==1:
        liste3.append(liste2[i])
    lpresent=0

print(liste3)          #Rien à voir ici, pas de meurtre dans le corpus réduit "corpus2.txt", à toi de jouer avec un vrai corpus !

