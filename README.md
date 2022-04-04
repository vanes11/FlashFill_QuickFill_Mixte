# FlashFill_QuickFill_Mixte

**FlashFill_QuickFill_Mixte** est une implémentation de trois algorithmes de synthèse de programmes (Flashfill Light, QuickFill et QuickMixte) avec une interface associée. Ces algorithmes prennent en entrée un ensemble d’exemples de couples (entrée, sortie) de chaînes de caractères et retourne des programmes (dans un DSL de manipulation des chaînes de caractères) P tel que P(entrée) = sortie pour chaque couple (entrée, sortie).

**Flashfill Light** une version simplifiée de l'algorithme FlashFill existant et disponible dans les versions MS Excel à partir de 2010. Pour son fonctionnement de FlashFill disponible dans l'article "**Automating String Processing in Spreadsheets Using Input-Output Examples** by Sumit Gulwani".

**QuickFill** est approche d’implémentation de FlashFill qui vise à élaguer l'espace de programmes de ce dernier. En effet, FlashFill explore un grand espace de programmes. L’intuition de QuickFill est que si l’utilisateur affine les spécifications (exemple entrée-sortie) en faisant des associations entre les sous-parties de la sortie et de l'entrée (couples de blocs), ceci permettra de réduire l’espace de programmes de FlashFill. Dans certains cas, ceci permettra de réduire le nombre d’exemples entrée-sortie avec l'avantage d'un temps d'exécution et une utilisation mémoire reduits.

**QuickMixte**, tout comme QuickFill a pour but la reduction du nombre de programmes retournés par FlafhFill. L'idee ici est de faire appel à FlashFill sur les couples de blocs. Cette approche montre particulièrement l'umpacte de la recherche d'une sous-chaine dans une chaine beaucoup plus longue.

-> **Installation sur unbuntu**

Installation de pip3,python3, nodejs et npm :

sudo apt update

sudo apt install python3-pip python3

sudo apt install nodejs npm

sudo apt install graphviz

Se deplacer vers le dossier frontend et exécuter la commande : npm install

Se deplacer dans le dossier backend et exécuter la commande : pip3 install -r requirements.txt

-> **Exectution** : lancer les serveurs du frontend et du backend dans deux consoles differentes.

Se deplacer dans le dossier backend et exécuter la commande : python3 manage.py runserver
Se deplacer dans le dossier frontend et exécuter la commande : npm run serve

Cliquer sur le lien de la forme : http://localhost:8080/

Voir video suivante https://drive.google.com/file/d/1OjzXLlZ759mxrcPyAT3bEDVBX6wfs0wE/view pour la démo sur l’utilisation de l’interface. Il faut noter que dqns cette vidéo, QuickMixte n'était pas encore disponible. Toutefois, tout se passe en interface comme pour QuickFill, une fois le bouton QuickMixte lancé.
