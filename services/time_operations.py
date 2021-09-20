import pandas as pd
from utils import *

class TimeOperations:

    def time_lag(self,x,y, delta,ocean):
        x = x[x.columns[:len(x.columns)-delta]]
        y = y[y.columns[delta:]]
        lags = {}
        for i in x.index:
            lags["TSM-"+ocean+x.loc[x.index[int(i)-1]].name+"("+str(delta)+")"] = x.loc[x.index[int(i)-1]].values
        for r in y.index:
            lags["PRM"+y.loc[y.index[int(r)-1]].name] = y.loc[y.index[int(r)-1]].values 
        return pd.DataFrame(lags)
    
    def generate_displacement(self,data_in,data_out,ocean_flag):
        flags = {"ATLN": "AN", "ATLS": "AS", "PCS": "PS", "NINO": "NI"}
        # out_columns = ["PRM1","PRM2","PRM3","PRM4","PRM5","PRM6","PRM7","PRM8","PRM9","PRM10","PRM11",
        #          "PRM12","PRM13","PRM14","PRM15","PRM16","PRM17","PRM18","PRM19","PRM20","PRM21",
        #          "PRM22","PRM23","PRM24"]
        DELTA = {}
        for r in range(1,13):
            x = data_in[data_in.columns[:len(data_in.columns) - r]].T
            y = data_out[data_out.columns[r:]].T
            columns = []
            for c in x.columns:
                columns.append("TSM-"+flags[ocean_flag]+str(c)+"("+str(r)+")")
            x.columns = columns
            y.columns = LABELS_SAIDAS
            DELTA["DELTA "+str(r)] = {"X": x, "y": y}  
        return DELTA