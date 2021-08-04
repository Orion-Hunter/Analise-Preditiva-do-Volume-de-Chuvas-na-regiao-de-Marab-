import pandas as pd
import numpy as np
import sys

sys.path.insert(0, '../settings');

from settings import config

class Precipitacao:
    data = None
    
    def __init__(self):
      self.data = pd.read_excel(config.URL_PANOM_MENSAL_CATEGORIZADA)
      self.data.rename(columns=self.data.iloc[0], inplace=True)
      self.data = self.data.drop(self.data.index[0])
      self.data.columns = ['Data','1','2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19', 
                               '20','21','22','23', '24']
      mascara = (self.data['Data'] >= '1982-01-01') & (self.data['Data'] <= '2020-12-01')
      self.data = self.data[mascara]
      self.data.name = 'PRECIPITACAO'
    
    def means(self):  
        res = []
        indexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                   '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        for r in self.data[indexes].columns:
            res.append(np.mean(self.data[r]))
        return res
