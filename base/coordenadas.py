import pandas as pd
import sys
import numpy as np 
from .precipitacao import Precipitacao
import plotly.express as px

sys.path.insert(0, '../settings');

from settings import config

class Coordenadas:
    data = None
        
    def __init__(self):
       self.data = pd.read_excel(config.URL_COORDENADAS)
       self.data.name = 'COORDENADAS'
     
    
    def transform(self):
        LAT_DEC = []
        LON_DEC = []
        MAPS = []
        PRECIPITACAO = Precipitacao()
        indices = np.linspace(1,24,24, dtype="int64") 
        for index, item in self.data.iterrows():
            casting_lat = item['LAT'].split(' ')[0]
            casting_lat = casting_lat.split(',')
            casting_lat = casting_lat[0]+"."+casting_lat[1]
    
            casting_lon = item['LON'].split(' ')[0]
            casting_lon = casting_lon.split(',')
            casting_lon = casting_lon[0]+"."+casting_lon[1]
    
            LAT_DEC.append(-float(casting_lat))
            LON_DEC.append(-float(casting_lon))
    
            MAPS.append("-"+casting_lat+"0000,-"+casting_lon+"0000")

        self.data['PRP_MEDIA'] = PRECIPITACAO.means()
        self.data['LAT_DEC'] = LAT_DEC
        self.data['LON_DEC'] = LON_DEC
        self.data['MAPS'] = MAPS  
        self.data = self.data.set_index(indices)
        
        
    # def draw_map(self):
    #     self.transform()
    #     fig = px.scatter_mapbox(self.data, lat="LAT_DEC", lon="LON_DEC", hover_name="ÁREA", hover_data=["PRP_MEDIA"],
    #                     color_discrete_sequence=["fuchsia"], zoom=5, height=300)
    #     fig.update_layout(mapbox_style="open-street-map")
    #     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #     fig.show()