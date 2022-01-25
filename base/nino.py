import pandas as pd
#import sys

#sys.path.insert(0, '../settings');

from config import URL_NINO

class Nino:
    data = None
        
    def __init__(self):
        self.data = pd.read_excel(URL_NINO)
        #NINO original columns = [NINO1+2, NINO3, NINO4, NINO3.4]
        self.data.columns = ['Data', '1', '2', '3', '4']
        mascara = (self.data['Data'] >= '1982-01-01') & (self.data['Data'] <= '2020-12-01')
        self.data = self.data[mascara]
        self.data = self.data.set_index('Data')
        self.data.name = 'NINO'
    
    
    def transpose_to_time(self):
        self.data = self.data.T
        self.data.rename(columns=self.data.iloc[0], inplace=True)
        self.data = self.data.drop(self.data.index[0])