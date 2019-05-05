from urllib.request import urlopen, hashlib, time

# Une petite fonction pour un timer entre les 2 méthodes (locale et distante).
def sleeper(num):
    while True:
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            continue
 
        # lance la commande time.sleep() et affiche le timestamp de début et de fin.
        print('Programme en pause à: %s' % time.ctime())
        time.sleep(num)
        print('Reprise du programme à: %s\n' % time.ctime())
        return False

# Valeur du mot de passe à tester
motdepass = input("Renseiger le mot de passe à tester.\n>")

# On le Hash avec SHA1 et on memorise sa valeur
hash_SHA1 = hashlib.sha1(bytes(motdepass, 'utf-8')).hexdigest()

#################################################
# On recupère un dico de mots de passe courrant #
# Plusieurs méthodes possibles !!!              #
#################################################
# dictionnaire_crack_01 = open('1_mille_knows_password_1000.txt', mode = 'r', buffering = 1, newline = '\n', encoding = 'utf-8')
# dictionnaire_crack_02 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

########################################################################
# Avec la fonction native "open" si le fichier est stocké en local:    #
# on utilise "with" pour s'assurer que le fichier ne reste pas ouvert. #
# Celui-ci ne contient que 1 million de mots (8meg environ)...         #
########################################################################
with open('1_million_knows_password_1000000.txt', mode = 'r', buffering = 1, newline = '\n', encoding = 'utf-8') as dictionnaire_crack_01:
    
    # On boucle tant qu'on est pas arrivé à la fin du DICO
    for to_easy in dictionnaire_crack_01:

        # On boucle encore, mais pour 1 mot = 1 ligne...
        for cracked_pass in to_easy.split ():

            # On Hash chaque mot de passe du DICO
            hash_DICO_01 = hashlib.sha1(bytes(cracked_pass, 'utf-8')).hexdigest()

            # On les compare
            if hash_DICO_01 == hash_SHA1:

            # Si les mots de passe sont semblable on les affiche et on stop la comparaison
                print("Mot de passe connue: ", str(cracked_pass))
                print("The Hash password input is: ", str(hash_SHA1))
                print("The Hash password found is: ", str(hash_DICO_01))
                quit()

            # Sinon on continue la recherche avec le mot de passe suivant dans le DICO
            elif hash_DICO_01 != hash_SHA1:
                print("Comparaison échouée! ", str(cracked_pass)," Test suivant...")

    # Le mot de passe n'est pas dans la liste.
    print("Le mot de passe ", "[ ", str(motdepass), " ]", " n'est pas encore connue !!!")

# Une petite pause de 5 seconds...
# On appel la fonction "sleeper" avec 10s en paramètre, équivalent à : "time.sleep(10)"
sleeper(10)

############################################################################
# Avec la fonction importée "urlopen" si le fichier est stocké sur le net: #
# On patiente en fonction de la taille du fichier...                       #
# On boucle en lisant les mots de passe du dico un par un (un par ligne)   #
############################################################################

# on importe un petit DICO pour le test:
dictionnaire_crack_02 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt').read(), 'utf-8')

for to_easy_02 in dictionnaire_crack_02.split('\n'):

    # On Hash chaque mot de passe du DICO
    hash_DICO_02 = hashlib.sha1(bytes(to_easy_02, 'utf-8')).hexdigest()

    # On les compare
    if hash_DICO_02 == hash_SHA1:

    # Si les mots de passe sont semblable on les affiche et on stop la comparaison
        print("Mot de passe connue: ", str(to_easy_02))
        print("The Hash password input is: ", str(hash_SHA1))
        print("The Hash password found is: ", str(hash_DICO_02))
        quit()

    # Sinon on continue la recherche avec le mot de passe suivant dans le DICO
    elif hash_DICO_02 != hash_SHA1:
        print("Comparaison échouée! ", str(to_easy_02)," Test suivant...")

# Le mot de passe n'est pas dans la liste.
print("Le mot de passe ", "[ ", str(motdepass), " ]", " n'est pas encore connue !!!")