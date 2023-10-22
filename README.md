**Projet** : SMILEY QUOKKA  
**Auteur** : Aurel MadBleiz  
**Contact** : aurel.bleuz@gmail.com  
**Objet** : open data of french DGDDI    

As part of Open Data, the DGDDI publishes data relating to trade French exterior. This data cannot be used as it stands, so I propose to clean these datasets.  
Data extraction and transformation are carried out in Python.  
The whole thing is distributed so that it can be containerized.  
If you have any advice, I'm interested ^^


#### PROCESS   
==============  


The default command is a bash script that downloads the data from the DGDDI website and then launches the main.py file.

**Build the image with podman**    
podman build -t smiley-quokka -f dockerfile  

**Run a container for the first time**   
podman run -it \  
    --name _foo_ \  
    -v data-volume:/usr/smiley-quokka/app/data \  
    smiley-quokka:latest  

**Run a container and a shell**   
podman run -it \  
    --name _foo_ \  
    -v data-volume:/usr/smiley-quokka/app/data \  
    smiley-quokka:latest bash  


#### DATA
=========

The datasets are in _./app/data/_  

**Fichier** : dgddi_national_data_2022.zip  
- national.csv : table of trades   
- a129.csv : table A129  
- cpf6.csv : table CPF6  
- nc8.csv : table NC8    
- pays.csv : table des pays
- LISEZ-MOI.txt : fichier d'origine  
- nc8_detail.xlsx : NC8 full  
- nc8_summary.xlsx : bill of materials summary  
- description.pdf : original description  


#### FIX  
====

**FIX_202310**  

- _001_ > Namibia wasn't codified --> add INSEE 'NAM'
- _002_ > Inconsistency with 'USUP' in 'NC8' --> replace NaN with '-'  
- _003_ > Encoding issue --> normalisation  
- _004_ > Drop duplicates


#### SOURCES  
=======  

Original datasets DGDDI : [Open Data](https://www.douane.gouv.fr/la-douane/opendata)
