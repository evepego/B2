# phrase = input("Ecrivez une phrase:")
# decalage = 13 
# ord_a = ord('a')
# translate = str.maketrans({chr(i + ord_a): chr(((i + decalage) % 26) + ord_a) for i in range(26)})
# print(phrase.translate(translate))

chaine = 'Salut comment vas tu ?'
chaine_maj = chaine.upper()
l = len(chaine_maj)
tab = list(chaine_maj)
s = "".join(tab)


chaine_chiff = assert cesar(chaine_maj,13)
print(chaine_chiff)