# from file_manager import *
import matplotlib.pyplot as plt
from covid_graphs import *


def main():
   
    countries = ['Spain',"Germany",'Italy']  
    

    # global_Con_Rec_Dead(countries, 'Europe', 'linear')    
    # global_Con_Rec_dead_first_day(countries, 'Europe', 'linear')
    
    # UK_Con_Rec_dead()
    #### US cases ####
    
  #   all_states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  # "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  # "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  # "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  # "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  # "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  # "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  # "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
    # the_south = ["Alabama",'Arkansas',"Florida","Georgia","Kentucky","Louisiana","Mississippi","Missouri","North Carolina","South Carolina","Tennessee",]
    # rise = ['Michigan', 'New Jersey', 'Florida']
  #   states = ['New York',"Oregon"]

    # US_con_dead_sums(['Kentucky','Georgia','Florida','New York'],'US','linear')
    # US_con_dead_sums(the_south, 'Rising','log')


    # graph_whole_world_con_dead(countries,'linear')

    graph_new_daily_change(['United States'],'linear')

    plt.show()
    
    return



if __name__ == "__main__":
    main()