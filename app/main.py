import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
data = pd.read_excel("./output/correlacoes/tabela_de_correlacoes.xlsx",index_col=[0])
data2 = pd.read_excel("./tsmxprecipitacao.xlsx", index_col=[0]).dropna()


def app():
        sel = st.sidebar.selectbox("Áreas de Precipitação", data.index)
        corr = pd.DataFrame({"TSM": data.loc[sel].index, "values": data.loc[sel].values })
        correlacoes_area = plt.figure(figsize=(10,8))
        correlacoes_area = px.histogram(corr, x='values', width=800)
        correlacoes_area.update_layout(title_text='Correlações '+sel, 
                                       title_x=0.5,
                                       showlegend=True,
                                       margin=dict(t=25, b=0, l=0, r=0),
                                    #    xaxis=dict(
                                    #        tickmode='array',
                                    #        tickvals= list(corr['values']),
                                    #        ticktext= list(corr['TSM']),
    
                                    #    )
                                       )
        st.plotly_chart(correlacoes_area, use_container_width=False)

def app2():
    sel = st.sidebar.selectbox("Visualizações", data2.columns)
    corr = pd.DataFrame({"TSM": data2[sel].index, "values": data2[sel].values })
    correlacoes_area = plt.figure(figsize=(10,8))
    correlacoes_area = px.line(corr, x='TSM', y='values',width=800)
    correlacoes_area.update_layout(title_text='Correlações '+sel, 
                                       title_x=0.5,
                                       showlegend=True,
                                       margin=dict(t=25, b=0, l=0, r=0),
                                    #    xaxis=dict(
                                    #        tickmode='array',
                                    #        tickvals= list(corr['values']),
                                    #        ticktext= list(corr['TSM']),
    
                                    #    )
                                       )
    st.plotly_chart(correlacoes_area, use_container_width=False)





sel = st.sidebar.selectbox("Visualizações", ['Histogramas', 'Séries Temporais'])

if sel == 'Séries Temporais':
    app2()
else:
    app()