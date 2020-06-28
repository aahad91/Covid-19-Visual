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
# ---Task Functions --- #


def multi_line_chart(data):
    data1_state_nrw = data.loc[data1['state']=='Nordrhein-Westfalen']
    data1_state_nrw['date'] = pd.to_datetime(data1_state_nrw['date'])
    data1_nrw_consolidated = data1_state_nrw.groupby([data1_state_nrw['date'].dt.date]).sum()
    Total_cases = data1_nrw_consolidated.cumsum(axis=0)
    Total_cases = Total_cases.rename(columns={"cases":"Total_confirmed_cases", "recovered":"Total_recovered_cases", 
                                        "deaths":"Total_death_cases"})
    return Total_cases

def bar_chart(data1, data2):
    nrw_data = data1[data1.state == 'Nordrhein-Westfalen']
    nrw_data.fillna(method='pad', inplace=True)
    nrw_data.age_group = nrw_data.age_group.str.replace('-', '_') 
    nrw_data = nrw_data.groupby('age_group')['cases'].apply(lambda x : x.sum()).reset_index()

    pop = data2[data2.state == 'Nordrhein-Westfalen']
    pop.age_group = pop.age_group.str.replace('-', '_')
    pop = pop.groupby('age_group')['population'].apply(lambda x : x.sum()).reset_index()
    nrw_data['population'] = pop['population']
    return nrw_data

def gp_bar_chart(data):
    df_nrw = data[data.state == 'Nordrhein-Westfalen']
    df_nrw.fillna(method='pad')
    df_nrw['age_group']=df_nrw['age_group'].str.replace('-','_')
    df_new=df_nrw.groupby(['county'])["cases", "deaths","recovered"].apply(lambda x : x.astype(int).sum()).reset_index()
    x = df_new['county']
    bar_plots = [
            go.Bar(x=x, y=df_new['cases'], name='Confirmed cases', marker=go.bar.Marker(color='orange'), visible = False),
            go.Bar(x=x, y=df_new['deaths'], name='Deaths', marker=go.bar.Marker(color='red'), visible = False),
            go.Bar(x=x, y=df_new['recovered'], name='Recovered cases', marker=go.bar.Marker(color='green'), visible = False)
        ]
    return bar_plots

def bubble_chart(data1, data3):
    pop = data1.loc[data1['state'] == 'Nordrhein-Westfalen']
    total_county = pop.county.unique()
    cases = []
    deaths = []
    recovered = []
    poulations = []

    for i in total_county:
        total_cases = 0
        total_deaths = 0
        total_recovered = 0
        cases_county=data1.loc[data1['county'] == i]
        for j in cases_county.cases:
            total_cases += j
        cases.append(total_cases)
        for k in cases_county.deaths:
            total_deaths += k
        deaths.append(total_deaths)
        for l in cases_county.recovered:
            total_recovered += l
        recovered.append(total_recovered)

    for m in total_county:
        pop_data = data3.loc[data3['county'] == m]
        for n in pop_data.population:
            poulations.append(n)
        
    df = pd.DataFrame() 
    df.insert(0, "county", total_county, True) 
    df.insert(1, "total_cases", cases, True) 
    df.insert(2, "total_deaths", deaths, True) 
    df.insert(3, "total_recovered", recovered, True) 
    df.insert(4, "population", poulations, True) 

    ratio = []
    for p in df.county:
        ratio_county=df.loc[df['county'] == p]
        ratio_s = float(ratio_county.total_cases/ratio_county.population)
        ratio.append(ratio_s) 

    df.insert(5, "ratio", ratio, True)
    return df

def dashboard(data1, data2, data3):
    # polished data for plots
    nrw_data = bar_chart(data1, data2)
    df = bubble_chart(data1, data3)
    Total_cases = multi_line_chart(data1)

    fig = go.Figure()
    # Bar Chart
    fig1 = go.Figure()
    # Bubble Chart
    fig2 = go.Figure()
    # Group Bar Chart
    fig3 = go.Figure(data=gp_bar_chart(data1))
    # Multi-line Chart
    fig4 = go.Figure()


    fig1.add_trace(go.Bar(x=nrw_data.age_group, y=nrw_data.population,name='Cases',
                    textposition='outside',texttemplate='%{text:.2s}', text=nrw_data.cases, 
                    hovertext='Age Group, Population',marker_color=px.colors.qualitative.Set1))
    
    s=0
    for j in df.county:
        fig2.add_trace(go.Scatter(x=df.loc[df['county'] == j].population,
                        y=df.loc[df['county'] == j].total_cases, name=j, 
                        text=j, visible = False,mode='markers',                 
                        marker=dict(size=df.loc[df['county'] == j].total_cases/15,color=s)))
        s+= 1

    fig4.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_confirmed_cases, 
                    name='Total_confirmed_cases', line=dict(color='royalblue', width=4, 
                    dash='dot'),visible = False))
    fig4.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_recovered_cases, 
                    name = 'Total recovered cases', line=dict(color='green', width=4, 
                    dash='dash'), visible = False))
    fig4.add_trace(go.Scatter(x=Total_cases.index, y=Total_cases.Total_death_cases, 
                    name='Total_death_cases', line=dict(color='red', 
                    width=4, dash='dashdot'), visible = False))

    visible_arr = []
    visible_arr1 = []
    visible_arr2 = []
    visible_arr3 = []
    visible_arr.append(True)
    visible_arr1.append(False)
    visible_arr2.append(False)
    visible_arr3.append(False)

    # Switching between graphs -> Start
    fig.add_trace(fig1.data[0])
    g=0
    for m in df.county:
        fig.add_trace(fig2.data[g])
        g += 1
        visible_arr.append(False)
        visible_arr1.append(True)
        visible_arr2.append(False)
        visible_arr3.append(False)

    fig.add_trace(fig3.data[0])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    visible_arr3.append(False)
    fig.add_trace(fig3.data[1])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    visible_arr3.append(False)
    fig.add_trace(fig3.data[2])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    visible_arr3.append(False)
    
    fig.add_trace(fig4.data[0])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(False)
    visible_arr3.append(True)
    fig.add_trace(fig4.data[1])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(False)
    visible_arr3.append(True)
    fig.add_trace(fig4.data[2])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(False)
    visible_arr3.append(True)
    # Switching between graphs <- End

    # Annotation for Bar Chart
    annotation1=[
            dict(
                x=0.50,
                y=-0.09,
                showarrow=False,
                text="Age Group",
                xref="paper",
                yref="paper",
                textangle=0
            ),
            dict(
                x=-0.07,
                y=0.5,
                showarrow=False,
                text="population",
                textangle=-90,
                xref="paper",
                yref="paper"
            )
    ]
    # Annotation for Bubble chart
    annotation2=[
            dict(
                x=0.50,
                y=-0.1,
                showarrow=False,
                text="Population",
                xref="paper",
                yref="paper",
                textangle=0
            ),
            dict(
                x=-0.07,
                y=0.5,
                showarrow=False,
                text="Total Cases",
                textangle=-90,
                xref="paper",
                yref="paper"
            )
    ]
    # Annotation for Group Bar Chart 
    annotation3=[
            dict(
                x=0.50,
                y=-0.25,
                showarrow=False,
                text="Counties",
                xref="paper",
                yref="paper",
                textangle=0
            ),
            dict(
                x=-0.07,
                y=0.5,
                showarrow=False,
                text="Total Cases",
                textangle=-90,
                xref="paper",
                yref="paper"
            )
    ]
    # Annotation for Multi-line Chart
    annotation4=[
            dict(
                x=0.50,
                y=-0.115,
                showarrow=False,
                text="Date",
                xref="paper",
                yref="paper",
                textangle=0
            ),
            dict(
                x=-0.07,
                y=0.5,
                showarrow=False,
                text="Total Cases",
                textangle=-90,
                xref="paper",
                yref="paper"
            )
    ]
    fig.update_layout(
        # Dropdown menu setting
        updatemenus=[
            dict(
                active=0,
                buttons=list([   
                    dict(label="By Age Group",
                        method="update",
                        args=[{"visible": visible_arr},
                            {"title": "Nordrhein-Westfalen Covid-19 Dashboard: View by Age Group, Population, Counties and Date", 
                            "annotations":annotation1}]),
                    dict(label="By Population",
                        method="update",
                        args=[{"visible": visible_arr1},
                            {"title": "Nordrhein-Westfalen Covid-19 Dashboard: View by Age Group, Population, Counties and Date", 
                            "annotations":annotation2}]),
                    dict(label="By County ",
                        method="update",
                        args=[{"visible": visible_arr2},
                                {"title": "Nordrhein-Westfalen Covid-19 Dashboard: View by Age Group, Population, Counties and Date", 
                                "annotations":annotation3}]),
                    dict(label="By Date",
                        method="update",
                        args=[{"visible": visible_arr3},
                                {"title": "Nordrhein-Westfalen Covid-19 Dashboard: View by Age Group, Population, Counties and Date", 
                                "annotations":annotation4}])
                ]),
            )
        ])
    fig.update_layout(title_text="Nordrhein-Westfalen Covid-19 Dashboard: View by Age Group, Population, Counties and Date",
                        height=1000,width=1800)
    fig.show()
# --------------------- #
if __name__ == "__main__":
    
    data1 = pd.read_csv('data/covid_de.csv')
    data2 = pd.read_csv('data/demographics_de.csv')
    data3 = pd.read_csv('data/counties_population.csv')

    dashboard(data1, data2, data3)