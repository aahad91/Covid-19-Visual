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
import plotly.graph_objs as go
from plotly.offline import plot

# ---Task Functions --- #


def multi_line_chart(data1):
    # Bhagyashree
    # data preprocessing
   data1_state_nrw = data1.loc[data1['state']=='Nordrhein-Westfalen']
   data1_state_nrw['date'] = pd.to_datetime(data1_state_nrw['date'])
   data1_nrw_consolidated = data1_state_nrw.groupby([data1_state_nrw['date'].dt.date]).sum()
   Total_cases = data1_nrw_consolidated.cumsum(axis=0)
   Total_cases = Total_cases.rename(columns={"cases":"Total_confirmed_cases", "recovered":"Total_recovered_cases", "deaths":"Total_death_cases"})
   
   # Visualization of plot
   figure = px.line(Total_cases, x=Total_cases.index, y=['Total_confirmed_cases', 'Total_death_cases', 'Total_recovered_cases'])
   figure.update_layout(title=' Total Growth of Cases (confirmed, recovered, death) for NRW',
                   xaxis_title='Date',
                   yaxis_title='Total_cases',
                   xaxis_tickformat = '%d/%m/%Y',font=dict(family='Arial', color='black', size=15), legend_title_text='',
                   legend=dict(x=0.2, y=-0.6,orientation='h',font=dict(family='Arial', color='black', size=20)))
   figure.update_traces(mode='lines+markers', marker_line_width=2, marker_size=8)
   figure.update_xaxes(rangeslider_visible=True, tickangle=-45, tickfont=dict(family='Arial', color='black', size=15))
   figure.update_yaxes(tickfont=dict(family='Arial', color='black', size=15))
   plot(figure, filename='multiseries.html')

#def bar_chart(data):
    #Ahad

#def gp_bar_chart(data):
    #Suganthi

def scatter_plt(data1):
    # Bhagyashree
    # data preprocessing
    data1_state_nrw = data1.loc[data1['state']=='Nordrhein-Westfalen']
    data1_nrw_updated = data1_state_nrw.fillna(method ='pad')
    data1_nrw_scatter = data1_nrw_updated.groupby(['age_group','gender']).sum()
    data1_nrw_scatter = data1_nrw_scatter.reset_index()
    data1_nrw_scatter['age_group'] = data1_nrw_scatter['age_group'].str.replace('-', '_')
    
    # Visualization of plot
    fig = go.Figure()
    figure2 = px.scatter(data1_nrw_scatter, x="age_group", y=["cases"], color="gender", symbol="gender", color_discrete_map={'F': 'darkgreen', 'M': 'darkblue'})
    
    figure3 = px.scatter(data1_nrw_scatter, x="age_group", y=["deaths"], color="gender", symbol="gender", color_discrete_map={'F': 'darkred', 'M': 'black'})
    
    figure4 = px.scatter(data1_nrw_scatter, x="age_group", y=["recovered"], color="gender", symbol="gender", color_discrete_map={'F': 'darkmagenta', 'M': 'brown'})
    

    s=0
    for i in data1_nrw_scatter.gender.unique():
       fig.add_traces(figure2.data[s])
       fig.add_traces(figure3.data[s])
       fig.add_traces(figure4.data[s])
       s+=1
    
    fig.update_xaxes(
    tickvals = ["00_04", "05_14", "15_34", "35_59","60_79", "80_99"],
    ticktext = ["00-04", "05-14", "15-34", "35-59","60-79", "80-99"], tickfont=dict(family='Arial', color='black', size=15))
  
    fig.update_yaxes(tickfont=dict(family='Arial', color='black', size=15))
    fig.update_layout(title='Gender wise (Male(M) / Female(F)) total cases per age-group for NRW',
                   xaxis_title='Age_group',
                   yaxis_title='Total_cases',
                   legend_title_text='', font=dict(family='Arial', color='black', size=15)
                   , legend=dict(x=0.43, y=-0.1, orientation='h', font=dict(family='Arial', color='black', size=20)))
    fig.update_traces(mode='markers', marker=dict(size=12))
    fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            type="buttons",
            direction="right",
            x=0.75,
            y=1.07,
            buttons=list([
                dict(label="Total_confirmed_cases",
                     method="update",
                     args=[{"visible": [True, False,False]},
                           ]),
                dict(label="Total_death_cases",
                     method="update",
                     args=[{"visible": [False, True, False]},
                           ]),
                dict(label="Total_recovered_cases",
                     method="update",
                     args=[{"visible": [False, False, True]},
                           ]),
                
            ]),
        )
    ])  
    plot(fig, filename='scatter.html')
    

#def bubble_chart(data1, data2):
    #Sayalee

#def dashboard(data1, data2):
    # for combining all plot and configuring dashbaord
    # Ahad
# --------------------- #
if __name__ == "__main__":
    print("Hello Everyone!!")
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad
    data1 = pd.read_csv('data/covid_de.csv')
    print(data1.head())
    
    multi_line_chart(data1)
    scatter_plt(data1)

    data2 = pd.read_csv('data/demographics_de.csv')
    print(data2.head())
