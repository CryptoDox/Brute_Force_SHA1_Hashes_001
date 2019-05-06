# DiscoPass - Hash et compare un mot de passe à partir d'un fichier texte.

# "DiscoPass.py" est largement commenté !

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Un petit programme en Python qui "Hash" un mot de passe avec SHA1 (mais ce pourrait être MD5), récupère une liste de mots de passe connu, "Hash" chacun des mots de passe, et procède à une comparaison.

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Il y a 2 méthodes, la première utilise un fichier texte local (facile à maintenir à jour), et l'autre récupère un fichier texte distant depuis internet. Ainsi nous pouvons observer les subtilités entre la fonction interne "open" et celle importée "urlopen".

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;On importe "urlopen", "hashlib" et "time". Donc vérifiez que ces 3 dépendances sont présentes en cas d'erreur...

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Il est possible d'augmenter la sécurité des mots de passe en vérifiant qu'ils ne sont pas trop communs ou carrément déjà connues, ce qui fragilise grandement la sécurité.

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Cet outil peut permettre de démontrer avec quelle facilité il est possible de mettre en œuvre des techniques de brute-forcing...

Il y a 2 fichiers texte fournit:

"1_mille_knows_password_1000.txt": contient mille mots de passe.

"1_million_knows_password_1000000.txt": contient un million de mots de passe.

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Sous licence M.I.T., vous pouvez utiliser/modifier le code selon votre bon vouloir. N'hesitez pas à me contacter, ce que vous en faite m'interesse !


Rejoignez-nous :&#160;<a href="http://diakonia.ddns.net" target="_blank">Site Web</a>&#160;|&#160;<a href="https://t.me/joinchat/FJWBVhD5IDEoVOWfMBSLBw" target="_blank">Groupe Telegram</a>&#160;|&#160;<a href="https://t.me/CryptoDox_Info" target="_blank">Canal Telegram</a>&#160;|&#160;<a href="https://t.me/CryptoDox_AirDropShare" target="_blank">Canal AirDrop Telegram</a>&#160;|&#160;<a href="https://www.facebook.com/groups/189000624988243/" target="_blank">Groupe Facebook</a>&#160;|&#160;<a href="https://twitter.com/Crypto_Dox" target="_blank">Twitter</a>&#160;|&#160;<a href="https://steemit.com/@cryptodox" target="_blank">Steemit</a>
