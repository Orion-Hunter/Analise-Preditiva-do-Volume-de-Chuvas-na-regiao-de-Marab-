import pandas as pd
import sys

sys.path.insert(0, '../settings');

from settings import config

class Nino:
    data = None
        
    def __init__(self):
        self.data = pd.read_excel(config.URL_NINO)
        self.data.columns = ['Data', 'NINO1+2', 'NINO3', 'NINO4', 'NINO3.4']
        mascara = (self.data['Data'] >= '1982-01-01') & (self.data['Data'] <= '2020-12-01')
        self.data = self.data[mascara]
        self.data.name = 'NINO'
