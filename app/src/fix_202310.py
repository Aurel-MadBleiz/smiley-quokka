import pandas as pd
import numpy as np
import unicodedata

def fix_2023_october(dgddi):
    """
    Apply 2023_october fix

    :param dataframe : dgddi dataframe
    :returns 0: cleaned dgddi dataframe
    :returns 1: Error
    """

    print("\n--> FIX_202310 - OCTOBRE 2023")
    
    # *** Issue 001 - Namibia *** #
    
    # < pays > table
    mask = dgddi['pays'].loc[:,'libelle'] == 'Namibie'
    dgddi['pays'].loc[mask,'code_pays'] = 'NAM'

    # 'import / export' file
    dgddi['national_import'] = dgddi['national_import'].fillna('NAM')
    dgddi['national_export'] = dgddi['national_export'].fillna('NAM')

    # *** Issue 002 - USUP *** #
    
    # 'nc8' file
    mask = dgddi['nc8'].loc[:,'bool_usup'] == 0
    dgddi['nc8'].loc[mask,'usup'] = '-'

    # *** Issue 003 - Normalization *** #

    # normalize data in NFKC
    dgddi['cpf6'].loc[:,'libelle'] = dgddi['cpf6'].loc[:,'libelle'].map(lambda x: unicodedata.normalize('NFKC',x))
    dgddi['nc8'].loc[:,['usup','libelle']] = dgddi['nc8'].loc[:,['usup','libelle']].map(lambda x: unicodedata.normalize('NFKC',x))
    dgddi['a129'].loc[:,'libelle'] = dgddi['a129'].loc[:,'libelle'].map(lambda x: unicodedata.normalize('NFKC',x))

    # *** Issue 004 - Old referencies  *** #

    # 'pays' file
    mask = dgddi['pays'].loc[:,'fin'] == '999912'
    dgddi['pays'] = dgddi['pays'].loc[mask]
    
    return dgddi