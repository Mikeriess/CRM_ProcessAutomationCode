# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:25:21 2021

@author: Mike
"""





class sim:
    def __init__(self, settings):
        
        self.settings = settings #dictionary
        
        #print("Simulation settings:")
        #print(settings)
        
    def simulate_t(self):
        
        print("simulating one step: ")
        print(self.settings)
        
        #data = {"time":0,
        #        "var1":1,
        #        "var2":1,
        #        "var3":1}
        
        data = [1,2,3,4]
        
        return data
    
    

#testsettings = {"days":1,
#                         "type":1,
#                         "param1":1,
#                         "param2":1}


#sim1 = sim(testsettings)

#sim1.simulate_t()

"""

Various approaches:
    
    Markov chains:
    https://python.quantecon.org/finite_markov.html

    Hawkes process:
    https://arxiv.org/pdf/1507.02822.pdf
    
    Process mining literature:
        https://www.researchgate.net/publication/313387633_Generating_event_logs_for_high-level_process_models
        https://www.researchgate.net/publication/328337892_Process_Modelling_Based_on_Event_Logs
        
        Carmago, dumas and rojas;
        https://www.sciencedirect.com/science/article/pii/S0167923620300397
        
"""