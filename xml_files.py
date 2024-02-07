import os
from datetime import date
import pandas as pd

class ReadXml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) if arq.lower().endswith(".xml")]

    def nfe_data(self, xml):
        df = pd.read_xml(xml, xpath=".//infNME")

        if df.empty:
            return []
        data_emissao = date.today().strftime('%d/%m/%Y')
        df["DataEmissao"] = data_emissao
        df["Usuario"] = ''
        df["data_saida"] = ''
        return df.values.tolist()

if __name__ == "__main__":
    xml = ReadXml('ferramentas')
    all_files = xml.all_files()

    result = []

    for i in all_files:
        result.extend(xml.nfe_data(i))

    # Cria um DataFrame usando o Pandas
    columns = ["Mat","Loc", "Ico", "Nr", "Det", "CProd", "QCom", "XProd", "UCom", "DataEmissao", "data_saida", "Usuario"]
    df = pd.DataFrame(result, columns=columns)

    # Exibe o DataFrame
    print(df)  