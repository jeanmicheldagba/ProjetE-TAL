#text = open("Projet TAL/corpus.xml", "r")

#import re
from lxml import etree
corpus = etree.parse("Projet TAL/corpus.xml")
for name in corpus.xpath("/root/document/docId/sentence
    <sentences>"):
    print(user.text)









#textSplit = re.split(".", text.read())

#expReg = r"E.*"
#for mot in textSplit :
#    if (re.search(expReg, mot) != None ):
#        print(re.search(expReg, mot))
