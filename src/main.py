import pandas as pd
import os ## para manipular diretórios do sistema
import glob ## para manipular diretórios e nomes de arquivos em massa
import re ## para utilizar expressões regulares

# Variável para caminho do arquivo
folder_path = "src\\data\\raw"

# Salvando o path dos arquivos excel da pasta raw em um objeto
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

print(excel_files)

if not excel_files:
    print("Nenhum arquivos Excel(.xlsx) compatível encontrado!")
else:
    # Criando um dataframe vazio
    df = []

    #Ler cada um dos arquivos e realizar tranformações neles
    for file in excel_files:
    
        #sempre que tentar ler um arquivo verificar se conseguiu ler
        try:
            #ler o arquivo de excel
            df_file = pd.read_excel(file)

            #pegar o nome do arquivo
            file_name = os.path.basename(file)
            print(file_name)

            #Adicionar a coluna LOCATION no dataframe com o país descrito no nome do arquivo
            #location = 
            #df_file['Location'] = 

        except Exception as e:
            print(f"Erro ao ler o arquivo {file} : {e}")
        
