class PreProcessing:
    def gerar_base_de_dados_deslocada(self, data, label):
        base = {}
        for delta in range(1,13):
            vars = []
            for col in data.columns:
                vars.append(label+col+"("+str(delta)+")")
            desl = data.shift(delta)
            desl.columns = vars
            base[delta] = desl
        return base