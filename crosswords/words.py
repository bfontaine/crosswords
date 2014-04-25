#! /usr/bin/python3.2
# -*- coding: latin-1 -*-

# pyMots v0.2
#
# par Baptiste Fontaine
# http://bfontaine.net
#
# Licence GPL v3
#
# utilisation:
#       ./pymots.py mot[ mot ...]
#
# fichier associe:
#       mots_francais.txt
#

import re

WORDS_FILENAME = "mots_francais.txt"

def load_file():
    """
    Retourne la liste des mots du fichier
    WORDS_FILENAME.
    """
    try:
        f = open(WORDS_FILENAME, "r")
        ct = f.read()
        f.close()
        liste = ct.split("\n")
        return [li.lower() for li in liste if (li)]
    
    except IOError:
        return False


def filter_list(liste, hyphen=True):
    """
    Filtre (retourne une nouvelle liste) une liste de mots (enleve
    les accents, les tirets, les majuscules)
    """
    # no_accents = str.maketrans("âäéèêë€îïôöðøûüùŷÿ$ŀ",
    #                            "aaeeeeeiiooo ouuuyysl")
    
    new_liste = []
    for li in liste:
        # tmp = li.lower().translate(no_accents)
        tmp = li.lower().replace("æ", "ae")
        tmp = tmp.replace("œ", "oe")
        if (hyphen):
            tmp = tmp.replace("-", "")
        if (tmp):
            new_liste.append(tmp)
    
    return new_liste

def match_word(word, liste):
    """
    Retourne tous les mots de la liste qui correspondent au
    mot partiel entre. Ex:
        match_word("_on__u_", ["bonjour", "bonsoir"]) -> ["bonjour"]
    """
    
    word = filter_list([word], hyphen=False)
    if (word):
        pattern = word[0]
    else:
        return False
    
    pattern = "#" + re.sub("[^a-z]", "[a-z]", pattern) + "#"
    
    search = "#".join(filter_list(liste))
    
    matching = re.findall(pattern, search)
    
    if (matching):
        return matching
    return False


if (__name__ == "__main__"):
    
    from sys import argv
    
    if (not len(argv) > 1):
        exit()
    
    mots = argv[1:]
    
    if (len(mots) == 1):
        
        print("Chargement du dictionnaire...")
        liste = match_word(mots[0], load_file())
        
        if (liste):
            print("%d possibilite(s): " % len(liste))
            
            for e in liste:
                print ("-> %s" % e[1:-1])
        
        else:
            print("aucune possibilite.")

    else:
        print("Chargement du dictionnaire...")
        liste_fic = load_file()
        
        for i in range(len(mots)):
            
            mot = mots[i]
            
            print("Mot n°%d :\n" % i+1)
            
            liste = match_word(mots[0], liste_fic)
        
            if (liste):
                print("%d possibilite(s): " % len(liste))
                
                for e in liste:
                    print ("-> %s" % e[1:-1])
            
            else:
                print("aucune possibilite.")

