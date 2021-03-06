import matplotlib.pyplot as plt
from covid_plotting import *


def global_Con_Rec_Dead(regions,fig_name,yscale):
    ''' This is a graph that has the confirmed, recovered, and deaths. '''

    fig = plt.figure(num = f'{fig_name} confirmed, recovered and dead.',figsize = (10,7))
    
    plt.suptitle("Global confirmed, recovered, \n and dead.")
    
    url = get_url('confirmed','global')

    global_confirmed_df= get_global_covid_df(url)

    url = get_url('recovered','global')
    global_recovered_df = get_global_covid_df(url)
    
    url = get_url('deaths','global')
    
    global_dead_df = get_global_covid_df(url)
    
    # print(global_dead_df)
    
    
    days_tick = 12 #days between tick marks
    
    l = len(global_recovered_df.T)
    start = 40  # day number past epoch to start plotting
 
    plt.subplot(311) 
    plot_global_regions(global_confirmed_df, 'confirmed', regions, start)
    plt.title('Confrimed')
  
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')
 
    plt.legend(loc = 'upper left') # This puts the legend in the top graph

    plt.subplot(312) 

    plot_global_regions(global_recovered_df,'recovered', regions, start)

    plt.title('Recovered')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')

    plt.subplot(313) 

    plot_global_regions(global_dead_df,'dead', regions, start)

    plt.title('Dead')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')
    plt.xlabel('date')

    plt.subplots_adjust(hspace = 0.4)
    
    return 




def US_con_dead_sums(regions,fig_name,yscale):
    ''' Creates graph of US state sums '''

    fig = plt.figure(num = fig_name,figsize = (10,7))
    plt.suptitle(f'{fig_name} US confirmed, and dead\n totals by state.')

    url = get_url('confirmed','US')
    confirmed_US_df = get_us_covid_df(url)
    
    url = get_url('deaths','US')
    dead_US_df = get_us_covid_df(url)

    
    start = 40
    days_tick = 7
   

    l = len(confirmed_US_df.T)

    plt.subplot(211)

    plot_all_subregion_sums(confirmed_US_df,regions,start)
    
    plt.title('Confirmed cases')
    plt.xticks(range(0, l-start,days_tick))
    
    plt.yscale(yscale)
    plt.ylabel('people')

    plt.legend(loc = 'upper left')

    plt.subplot(212)

    plot_all_subregion_sums(dead_US_df,regions,start)

    plt.title('Deaths')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')
    plt.xlabel('date')

    plt.subplots_adjust(hspace = 0.4)
    
    return

def global_Con_Rec_dead_first_day(regions,yscale):
    ''' This is a graph that has the confirmed, recovered, and deaths. '''

    fig = plt.figure(num = 'Global confirmed, recovered and dead.',figsize = (10,7))

    plt.suptitle("Global confirmed, recovered \n and dead.")
    
    url = get_url('confirmed','global')
    global_df_confirmed = get_global_covid_df(url)

    url = get_url('recovered','global')
    global_recovered_df = get_global_covid_df(url)
    
    url = get_url('deaths','global')
    global_dead_df = get_global_covid_df(url)



    days_tick = 12 #days between tick marks
    yscale = 'linear'
    l = len(global_recovered_df.T)
    start = 40  # day number past epoch to start plotting
 
    plt.subplot(311) 

    plot_all_region_sums(global_df_confirmed,regions,start)
    
   
    plt.title('Confrimed')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')

    plt.legend(loc = 'upper left') # This puts the legend in the top graph

    plt.subplot(312) 

    plot_all_region_sums(global_recovered_df, regions, start)

    plt.title('Recovered')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')

    plt.subplot(313) 

    plot_all_region_sums(global_dead_df, regions,start)

    plt.title('Dead')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.ylabel('people')
    plt.xlabel('date')

    plt.subplots_adjust(hspace = 0.4)
    
    return 

def graph_daily_new_cases(df):
        # print(df)
    
        return

def graph_whole_world_con_dead(regions,yscale):
    ''' combine both dfs and graph.'''

    url = get_url('confirmed','global')
    global_df_confirmed = get_global_covid_df(url)
    
    url = get_url('deaths','global')
    global_dead_df = get_global_covid_df(url)

    url = get_url('confirmed','US')
    confirmed_US_df = get_us_covid_df(url)
    # confirmed_US_df = add_sum_column_US_df(confirmed_US_df)

    url = get_url('deaths','US')
    dead_US_df = get_us_covid_df(url)
    # dead_US_df = add_sum_column_US_df(dead_US_df)

    start = 5

    confirmed_df = get_whole_df(global_df_confirmed,confirmed_US_df)

    dead_df = get_whole_df(global_dead_df,dead_US_df)

    # plot_all_region_diffs(dead_df,regions,start)

    # plot_all_region_diffs(confirmed_df,regions,start)

    confirmed_df =  add_all_sum_columns(confirmed_df)
    dead_df = add_all_sum_columns(dead_df) 

    # print(dead_df.loc[['Canada','United Kingdom','United States']])
    # print(confirmed_df.loc[['Canada','United Kingdom','United States']])




def graph_new_daily_change(regions,yscale):

    url = get_url('confirmed','global')
    global_df_confirmed = get_global_covid_df(url)
    
    url = get_url('confirmed','US')
    confirmed_US_df = get_us_covid_df(url)

    url = get_url('deaths','global')
    global_df_dead = get_global_covid_df(url)
    
    url = get_url('deaths','US')
    dead_US_df = get_us_covid_df(url)

    fig = plt.figure(num = 'Daily Change.', figsize = (10,7))

    window_size = 7
    start = 50
    days_tick = 7 

    # print(confirmed_daily_df.loc['United States'])
    plt.subplot(211)
    l = len(plot_daily_change(global_df_confirmed,confirmed_US_df,regions,start,window_size).T)

    # l = len(confirmed_daily_df.T)

    plt.title('New Cases Confirmed daily')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.legend()
    plt.ylabel('confirmed caseses')
    plt.xlabel('date')

    plt.subplot(212)
    l = len(plot_daily_change(global_df_dead,dead_US_df,regions,start,window_size).T)

    # l = len(dead_daily_df.T)

    plt.title('Deaths')
    plt.xticks(range(0, l-start,days_tick))
    plt.yscale(yscale)
    plt.legend()
    plt.ylabel('Deaths')
    plt.xlabel('date')


