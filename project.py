"""
Assignment-5: Covid-19 Visualization
Group-11
Members: Abdul Ahad Ayaz, Sayalee Chavan, Suganthi Jaganathan,
Bhagyashree Sanjay Borade
"""

# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import warnings
# ---Task Functions --- #
warnings.simplefilter("ignore")

def multi_line_chart(data):
    #Bhagyashree 
    #Modified by Suganthi according to the new requirements
    #Data Preprocess
    data1 = pd.read_csv(r"H:\IDV_lab\covid_de.csv")
    data1_state_nrw = data1.loc[data1['state']=='Nordrhein-Westfalen']
    data1_state_nrw['date'] = pd.to_datetime(data1_state_nrw['date'])
    data1_nrw_consolidated = data1_state_nrw.groupby([data1_state_nrw['date'].dt.date]).sum()
    Total_cases = data1_nrw_consolidated.cumsum(axis=0)
    Total_cases = Total_cases.rename(columns={"cases":"Total_confirmed_cases", "recovered":"Total_recovered_cases", "deaths":"Total_death_cases"})
    print(Total_cases.index)
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_confirmed_cases, name='Total_confirmed_cases',
                             line=dict(color='yellow', width=4)))
    fig.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_recovered_cases, name = 'Total recovered cases',
                             line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_death_cases, name='Total_death_cases',
                             line=dict(color='salmon', width=4,
                                  dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
    ))
    
    fig.update_layout(title='Covid-19 Visualization in NRW',
                       xaxis_title='Date',
                       yaxis_title='Total Cases')
    
    
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    return fig

def bar_chart(data1, data2):
    #Ahad
    
    return bar
def gp_bar_chart(data1):
    #Suganthi
#Preprocessing the data
    df_nrw = data1[data1.state == 'Nordrhein-Westfalen']
    df_nrw.fillna(method='pad')
    df_nrw['age_group']=df_nrw['age_group'].str.replace('-','_')
    df_new=df_nrw.groupby(['county'])["cases", "deaths","recovered"].apply(lambda x : x.astype(int).sum()).reset_index()
    #Visualizing the data
    x = df_new['county']
    bar_plots = [
        go.Bar(x=x, y=df_new['cases'], name='Confirmed cases', marker=go.bar.Marker(color='#FFA07A')),
        go.Bar(x=x, y=df_new['deaths'], name='Deaths', marker=go.bar.Marker(color='#C71585')),
        go.Bar(x=x, y=df_new['recovered'], name='Recovered cases', marker=go.bar.Marker(color='#0000FF'))

    ]
    layt = go.Layout(
        title=go.layout.Title(text="Covid-19 Visualization in NRW county"),
        yaxis_title="TOTAL CASES",
        xaxis_title="COUNTY",
        xaxis_tickvals=df_new.county,
        xaxis_ticktext=tuple(df_new['county'].values),
    )       
    fig = go.Figure(data=bar_plots, layout=layt)
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    return fig

#def scatter_plt(data):
    #Bhagyashree

#def bubble_chart(data1, data2):
    #Sayalee

def dashboard(data1,data2):
    
# --------------------- #
    if __name__ == "__main__":
        
        gp_bar_chart(data1)
        
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad

#    
     

#    bar_chart(data1, data2)
data1 = pd.read_csv('data\covid_de.csv')
data2 = pd.read_csv('data\demography.csv')    
dashboard(data1,data2)
