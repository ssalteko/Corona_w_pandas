import pandas as pd
def get_url(dtype, region):
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{dtype}_{region}.csv'
    
    return url


def get_global_covid_df(file_name):
    '''creates a df from covid data.'''

    df = pd.read_csv(file_name)
    df = df.drop(['Lat','Long'], axis = 1)
    df['Population'] = 0
    df['Admin2'] = None
 
    columns = df.columns.tolist()      # Gets list of columns, from data frame with new column at the end.
    columns.insert(2, columns.pop(-1))
    columns.insert(3, columns.pop(-1)) # Sets the new column name to a location while deleting its own previous entry from the same list.  

    df = df[columns]

    return df

def get_UK_covid_w_sub_regions_df(file_name):
    '''creates a df from covid data.'''

    df = pd.read_csv(file_name)
    df = df.loc[df['Country/Region'] == 'United Kingdom'] ## finds all rows with value UK in country/region
    df = df.drop(['Lat','Long'],axis = 1)
    
    return df


def get_us_covid_df(file_name):
    '''creates a df from covid data.'''
    
    df = pd.read_csv(file_name)
    df = df.drop(['UID', 'iso2','iso3','code3','Lat','Long_','FIPS','Country_Region','Combined_Key'], axis = 1)
    df = df.rename(columns={'Province_State': 'Province/State'})
    df['Country/Region'] = 'United States'
    
    columns = df.columns.tolist()
    columns.insert(2, columns.pop(-1)) #Move the last element to a place in the list without itself
    columns.insert(2, columns.pop(0))

    df = df[columns]
    
    return df




def add_sum_column_for_subregion(df,subregions):
    ''' Creates another column with the sums of the multiple regions within an country.'''

    #### Make the df only have the regions of interest

    #TODO add the below function for compactnes. 
    # df = df[df['Country/Region'].isin(regions)]

    df2 = pd.DataFrame()
    
    for region in subregions:
    
        df1 = df[df['Province/State'] == region]
        df2 = pd.concat([df2,df1])
    df = df2.reset_index()

    ### Groupby sum of with simlar province/state, will this will cause problems when a country has multiple regions?
    df1 = df.groupby('Province/State', axis = 0).sum().reset_index()

    ###Change the cell value so that it has the proper column title in the final transposed df/array.
    subregions_t = []
    for region in subregions:
        subregions_t += [f'{region} sum']
    subregions_t.sort()
    df1.loc[:,'Province/State'] = subregions_t
        
    ### Concatinate the origional df and the sum_df by vertically.
    df = pd.concat([df,df1]).set_index('Province/State').T
    df = df.drop(['index'], axis = 0)

    return df

def add_sum_column_for_region(df,regions):
    ''' Creates another column with the sums of the multiple countires with multiple colonies.'''

    #### Make the df only have the regions of interest
    #TODO add the below function for compactnes. 
    # df = df[df['Country/Region'].isin(regions)]
    
    df2 = pd.DataFrame()

    for region in regions:
    
        df1 = df[df['Country/Region'] == region]
        df2 = pd.concat([df2,df1])
    df = df2.reset_index()

    ### Groupby sum of with simlar province/state, will this will cause problems when a country has multiple regions?
    df1 = df.groupby('Country/Region', axis = 0).sum().reset_index()

    ###Change the cell value so that it has the proper column title in the final transposed df/array.
    regions_t = []
    for region in regions:
        regions_t += [f'{region} sum']
    
    df1.loc[:,'Country/Region'] = regions_t
        
    ### Concatinate the origional df and the sum_df by vertically.
    df = pd.concat([df,df1]).set_index('Country/Region').T
    df = df.drop(['index'], axis = 0)
    
    return df



def add_diff_column_for_region(df,regions):
    ''' Creates another column with the sums of the multiple countires with multiple colonies.'''
    df_orig = df
    
    df = df[df['Country/Region'].isin(regions)] #### Make the df only have the regions of interest
    
    regions_t = list(map(lambda x:f'{x} diff',regions))
   
    regions_t = sorted(regions_t)

    df = df.reset_index()
    
    df1 = df.T[5:].diff(axis = 0) ###Take the diff of all the date columns.
    
    df3 = df.T.iloc[0:5] ### Create a df head for uniformity.
    
    df3 = pd.concat([df3,df1]) ### Make the uniform df.

    df3.iloc[2] = regions_t  ### Set the values of the colmn
   
    ### Concatinate the origional df and the sum_df  vertically.
    df = df3.drop(['index'], axis = 0)
    df = pd.concat([df_orig,df.T])
    df = df.set_index(['Country/Region','Province/State','Admin2'])
    
    # print(df)
    return df
    
    
def get_whole_df(df1,df2):
    ''' Concats to dfs by columns'''
    df2 = get_US_sum_df(df2)
    df = pd.concat([df1,df2], axis = 0)

    # print(df.loc[df['Country/Region'] == 'United States All'])
    return df

def get_US_sum_df(df_US):
    '''Sums the entire US df'''

    df_orig = df_US

    df = df_US.groupby('Country/Region').sum()
    df = df.reset_index()
    
    df1 = pd.DataFrame([['NaN']], columns = ['Province/State'])

    df = pd.concat([df1,df],axis = 1)
    df.at[0,'Country/Region'] = 'United States All'
    
    df = pd.concat([df_orig,df])
    df = df.reset_index()

    df = df.drop(['index'], axis = 1)
    
    return df