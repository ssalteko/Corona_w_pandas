import matplotlib.pyplot as plt
from covid_panda import *
import pandas as pd

#### TODO fix multiple lables for countries with multi colonies

def plot_global_regions(df, dtype, regions,start):
    ''' plot global df and label for legend. '''
    
    df = df.set_index('Country/Region').T[regions]
    l = df.count()
    
    for region in regions:
        plt.plot(df[f'{region}'][start:], label = f'{region}',marker = "o")
    
  
def plot_all_subregion_sums(df,subregions,start):
    ''' adds sum column to df then plots those sums  given a df and a list of regions.'''
    
    df = add_sum_column_for_subregion(df,subregions)

    for subregion in subregions:
    
        plt.plot(df[f'{subregion} sum'][start:], label = f'{subregion} sum',marker = "o")

   

def plot_all_region_sums(df,regions,start):
    ''' adds sum column to df then plots those sums  given a df and a list of regions.'''
    
    df = add_sum_column_for_region(df,regions)
    
    for region in regions:
    
        plt.plot(df[f'{region} sum'][start:], label = f'{region} sum',marker = "o")



def plot_daily_change(df,regions,start):
    ''' Plots a bar graph of the daily change in the df.'''
    
    dates = list(df.keys())[1:]
    
    for region in regions:
  
        plt.bar(dates[start-1:],df.T[f'{region}'][start:], label = region,alpha = 1)
  