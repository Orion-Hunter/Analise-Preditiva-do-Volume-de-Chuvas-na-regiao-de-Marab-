import pandas as pd
from utils import *
from scipy import stats as st
##Operações de Seleção de Dados
class SelectionOperations:

    def generate_correlation_tables(self,data):
        CORR = {}
        data_list = []
        for k in data.keys():
            var = {}
            for x in data[k]['X'].columns:
                var[x] = []
                for y in data[k]['y'].columns:
                    c = st.kendalltau(data[k]['X'][x],data[k]['y'][y])[0]
                    var[x].append(c)
            CORR[k] = pd.DataFrame(var).T
            CORR[k].columns = LABELS_SAIDAS
        for k in CORR.keys():
            data_list.append(CORR[k])
        return pd.concat(data_list)
    
    def select_nvars(self, data, n):
        columns = data.columns
        selected = {}
        for r in data.index:
            data_abs = abs(data[r])
            indices = list(data_abs.sort_values(by=[r], ascending=False)[r].head(n).index)
            selected[r] = data.T[indices].columns
        return pd.DataFrame(selected)
    
    def find_var(self, var, out, data):
        col = list(data.columns)
        if var in col: 
            return data[[var,out]]
        return None
    

    def read_multiple_bases(self):
        bases = {}
        paths = ["Base_Atlantico_Norte.xlsx","Base_Atlantico_Sul.xlsx", "Base_Nino.xlsx", "Base_Pacifico_Sul.xlsx"]
        sheet_names = ['1','2','3','4','5','6','7','8','9','10','11','12']
        i = 0
        for p in paths:
            for s in sheet_names:
                bases[i+1] = pd.read_excel(p, s)
                i+=1
        return bases
        

    def select_data(self, data, n):
        selected_vars = self.select_nvars(data, n)
        var = {}
        vars_name = {}
        bases = self.read_multiple_bases()
        for v in selected_vars.columns:
            var[v] = []
            for i in selected_vars[v]:
                for k in bases.keys():
                    df = self.find_var(i,v,bases[k])
                    if df is not None:
                        var[v].append(df)
        for k in var.keys():
            vars_name[k] = []
            for i in range(0,len(var[k])):
                vars_name[k].append(var[k][i].columns[0])
        return vars_name, var