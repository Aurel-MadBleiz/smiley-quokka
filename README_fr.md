**Projet** : SMILEY QUOKKA  
**Auteur** : Aurel MadBleiz  
**Contact** : aurel.bleuz@gmail.com  
**Objet** : distribution des données issue de l'open data de la DGDDI    

Dans le cadre de l'Open Data, la DGDDI publie les données relatives au commerce extérieur français. Ces données ne sont pas exploitables en l'état aussi je propose de les nettoyer.  
L'extraction et la transformation des données sont réalisées en Python.  
L'ensemble est distribué de façon à pouvoir être conteneurisé.  
Si vous avez des conseils, je suis preneur ^^  


#### FONCTIONNEMENT  
==============  


<<<<<<< HEAD:README.md
Il est possible de procéder manuellement :  
1/ Téléchager les donnée 2022 nationale sur le site de la DGDDI[[1]](https://www.douane.gouv.fr/la-douane/opendata)  
2/ Extraire les fichiers dans un répertoire temporaire  
3/ Créer les répertoires < ./db/original > et < ./db/final >  
4/ Copier l'ensemble des fichiers <*.txt> excepté <LISEZ-MOI.txt> dans <./db/original/>  
5/ Exécuter <main.py>    
=======
La commande par défaut est un script bash qui télécharge les données sur le site de la DGDDI puis lance le fichier main.py.  
>>>>>>> 2f7966d (Major update):README_fr.md

**Construire l'image sous podman**    
podman build -t smiley-quokka -f dockerfile  

**Exécuter le container pour la première fois**   
podman run -it \  
    --name _foo_ \  
    -v data-volume:/usr/smiley-quokka/app/data \  
    smiley-quokka:latest  

**Exécuter le container avec un shell**   
podman run -it \  
    --name _foo_ \  
    -v data-volume:/usr/smiley-quokka/app/data \  
    smiley-quokka:latest bash  


#### DONNÉES
=========

Les tables se trouvent dans le dossier _./app/data/_  

**Fichier** : dgddi_national_data_2022.zip  
- national.csv : table des opérations  
- a129.csv : table A129  
- cpf6.csv : table CPF6  
- nc8.csv : table NC8    
- countries.csv : table des pays
- LISEZ-MOI.txt : fichier d'origine  
- nc8_detail.xlsx : fichier NC8 détaillée  
- nc8_summary.xlsx : fichier des principales sections et chapitres de la nomenclature  
- description.pdf : fichier d'origine  


#### FIX  
====

**FIX_202310**  

- _001_ > La Namibie n'était pas codifiée --> ajout du code INSEE 'NAM'
- _002_ > Incohérence dans la colonne 'USUP' du fichier 'NC8' --> l'absence d'usup se traduit par '-'  
- _003_ > Problème d'encodage --> normalisation  
- _004_ > Doublons dans le fichier pays causé par d'anciennes références --> suppresssion des références


#### SOURCES  
=======  

Donées originale DGDDI : [Open Data](https://www.douane.gouv.fr/la-douane/opendata)
