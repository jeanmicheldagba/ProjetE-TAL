import nltk
import re
a = open("corpus2.txt","r")
corpus=a.readlines()



def before(mot, corpus):
    a=corpus.split(mot)
    return(a[0])

def after(mot, corpus):
    a=corpus.split(mot)
    return(a[1])

def find(item, corpus):
    if item in corpus:
        return 1
    else:
        return 0


#temp=before(">PERSON<",corpus)
i=0
s=0
liste=[]
lemme=["assassinate","drown","execute","massacre","murder","poison","slaughter","slay","annihilate","asphyxiate","crucify","electrocute","finish","garrote","guillotine","immolate","liquidate","lynch","neutralize","smother","strangle","suffocate"]
for i in range(len(corpus)):
    if corpus[i].find("<sentence id=")!=-1: 
        s=int(before('"',after('"',corpus[i])))
    if corpus[i].find(">PERSON<")!=-1:
        if corpus[i-5].find("<word>E")!=-1:
            liste.append(s-1)
            liste.append(s)
            liste.append(s+1)

    
