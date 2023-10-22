import src.process as process
import src.fix_202310 as fix_2023
import json

def main():
    try:
        with open('./conf/csv_conf.json','r') as f:
            csv_conf = json.load(f)
        with open('./conf/hash_table.json','r') as f:
            hash_table = json.load(f)
    except FileNotFoundError as file_error:
        print(file_error)

    param = [csv_conf[k]['path'] for k in csv_conf.keys()]
    if process.compare_hash(hash_table,param) == 1:
        return 1
    
    print("\n*** Chargement des fichiers originaux ***\n")
    dgddi = process.load_csv(csv_conf)
    if dgddi == 1:
        print("Fichier non trouvé")
        return 1
    else:    
        print("\nTerminé")

    print("\n*** Application des correctifs ***")
    dgddi_fixed = fix_2023.fix_2023_october(dgddi)
    print("\nTerminé")

    print("\n*** Exportation des données ***")
    process.export_data(dgddi_fixed)
    print("\nTerminé")

    return None

if __name__ == '__main__':
    main()