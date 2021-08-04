import pandas as pd
import sys

sys.path.insert(0, '../settings');

from settings import config

class AtlanticoSul:
    data = None
        
    def __init__(self):
        self.data = pd.read_excel(config.URL_ATLA_S)
        self.data.rename(columns=self.data.iloc[0], inplace=True)
        self.data = self.data.drop(self.data.index[0])
        self.data.columns = ['Data','1','2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19', 
                           '20','21','22','23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
                           '37', '38', '39']
        mascara = (self.data['Data'] >= '1982-01-01') & (self.data['Data'] <= '2020-12-01')
        self.data = self.data[mascara]
        self.data.name = 'ATLANTICO_SUL'