#!/bin/bash

app_dir=/usr/smiley_quokka/app
import_file=202308-National-2022-import.zip
export_file=202308-National-2022-export.zip
import_url=https://www.douane.gouv.fr/sites/default/files/2023-10/06/$import_file
export_url=https://www.douane.gouv.fr/sites/default/files/2023-10/06/$export_file


# make directories and work in a temporary directory

cd $app_dir
mkdir tmp
cd tmp
# Retrieve data
wget $import_url
wget $export_url

if 7zz e -y $import_file && 7zz e -y $export_file ; then
    echo 
else
    echo "Erreur avec lors de l'extraction des fichiers"
    cd $app_dir && rm -fr ./tmp
fi

cd $app_dir
python main.py

# Clean up
rm -fr ./tmp
