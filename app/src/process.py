import pandas as pd
import numpy as np
import json
import os
import hashlib

def compare_hash(hash_table,file_list):
    """
    Controle the file integrity

    :param hash_table: json with the hash information
    :param file_list: list of data files
    """
    # Generate and compare hash
    for k in file_list:
        with open(k,'rb') as fb:
            hash_gen = hashlib.file_digest(fb,'sha256')
            split_file = os.path.split(k)
            if hash_gen.hexdigest() != hash_table[split_file[1]]:
                print(f"Erreur le fichier {split_file[1]} semble corrompu")
                return 1
    return 0
    
def load_csv(csv_conf):
    """
    Load the data

    :param csv_conf: csv_configuration
    :returns 0: Dataframe
    :returns 1: Error file
    """
    
    # Dictionary of data
    dgddi = {}

    # Loop throught file name
    for k in csv_conf.keys():
        file_path = csv_conf[k]['path']
        # If file exists
        if os.path.exists(file_path):
            file_split = os.path.split(file_path)
            print(f"{file_split[1]}...")
            dgddi[k] = pd.read_csv(
                file_path,
                **csv_conf[k]['parameters'])
        else:
            return 1        
    return dgddi

def export_data(dgddi):
    """
    Export the data into csv tables

    :param dgddi : cleaned dataframe
    :returns 0: None
    :returns 1: Error
    """

    # *** Concat 'national_import' and 'national_export' *** #
    
    df_national_merged = pd.concat([dgddi['national_import'],dgddi['national_export']])
    # Remove the old keys
    dgddi.pop('national_import')
    dgddi.pop('national_export')
    dgddi.update({'national':df_national_merged})
    
    # *** Export data *** #
    
    for k in dgddi.keys():
        file_path = f"./data/{k}.csv"
        dgddi[k].to_csv(
            file_path,
            index=False,
            sep='|',
            encoding='utf-8')    
    return 0
