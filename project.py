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

# ---Task Functions --- #


#def multi_line_chart(data):
    #Bhagyashree

def bar_chart(data):
    #Ahad
    data.age_group.unique()
    d2 = data[data.state == 'Nordrhein-Westfalen']
    print(d2.age_group.isna().sum())
    d2.fillna(method='pad', inplace=True)
    print(d2.age_group.isna().sum())
    d2.age_group = d2.age_group.str.replace('-', '_') 
    #print(d2[d2.age_group == '00_04'].groupby(d2.state == 'Nordrhein-Westfalen').cases.sum())
    #dic = {}
    #d2 = d2[['age_group', 'cases']]
    d3 = d2.groupby('age_group')['cases'].apply(lambda x : x.sum()).reset_index()
    # for i in d2.age_group.unique():

    print(d3.head())
    
    #d2.groupby([d2.age_group])['cases'].sum()
    #print(d2)
    fig = px.bar(d3, x='age_group', y='cases')
    fig.show()
#def gp_bar_chart(data):
    #Suganthi

#def scatter_plt(data):
    #Bhagyashree

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
    data2 = pd.read_csv('data/demographics_de.csv')

    bar_chart(data1)