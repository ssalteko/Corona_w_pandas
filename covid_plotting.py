import matplotlib.pyplot as plt
from covid_panda import *
import pandas as pd


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



def plot_daily_change(df1,df2,regions,start,window_size):
    ''' Plots a bar graph of the daily change in the df.'''
    
    df = get_whole_df(df1,df2)

    df = get_all_CountryRegion_sum_df(df)
    df = df.rename(index = {'Georgia':"Georgian Republic"})
    # print(df.iloc[50:100])
    # print('\n\ndf2 b4: \n\n',df2)
    df2 = get_all_StateProvince_sum_df(df2)
    # print('\n\n df2 aftr: \n\n',df2)
    df = pd.concat([df,df2])
    # print('\n\n df: \n\n',df)

    df = get_daily_change_df(df)
    # print(df.loc['Alabama'])
    df1 = df.rolling(window_size, axis = 1).mean()
    # df1 = df.rolling(window_size, axis = 1).median()
    # df3 = df1.rolling(2*window_size, axis = 1).median()
    # print(df1)
    # df = pd.concat([df,df2])
    # print(df)
    dates = list(df.keys())[1:]
    # print(dates)
    for region in regions:
        plt.bar(dates[start-1:],df.T[region][start:], label = region,alpha = 1)
        plt.plot(df1.T[region][start:], color = 'red')
        # plt.plot(df3.T[region][start:],color = 'black')

    return df
  