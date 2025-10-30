import os
import pandas as pd

def salvar(dir_arquivos, planilhas, planilhas_nomes):

    for planilha, nome in zip(planilhas, planilhas_nomes):

        dataframe = pd.DataFrame(planilha)
        arquivo = os.path.join(dir_arquivos, nome+'.csv')
        dataframe.to_csv(path_or_buf=arquivo, sep=';', index=False)
    