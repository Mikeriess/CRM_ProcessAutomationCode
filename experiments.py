# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:00:15 2021

@author: Mike
"""


class Experiment:
    import model
    import simulation as s
    import process_automation as p
    
    def __init__(self, DOE, run):
        
        # Data attributes of all experiments
        self.DOE = {"Factor1":[0,1],
                    "Factor2":[0,1]} # this is a dictionary
        
        
        # Simulation settings
        self.simulation_settings = {"days":1,
                         "type":1,
                         "param1":1,
                         "param2":1}
        
        # Automation settings
        self.automation_settings = "FIFO"
        
        # The ID of the run
        self.run = 0 # this contain the

    def save_data(self, destination):
        
        data = {"DOE":self.DOE,
                "run":self.run}
        print("data saved to" + destination)
        
        return data
  
    def run_experiment(self):
        """
        Here the sequence of an experiment is run
        """
        
        print("Running experiment " + str(self.run))
        
        # set up simulation object
        sim_t0 = self.s.sim(self.simulation_settings)
        
        # Simulate
        data_t = sim_t0.simulate_t()
        print(data_t)
        
        #############################################
        # Modelling
        #############################################
        
        # Create a model object
        mod1 = self.model.model("model type 1",
                                "hpo settings 1")
        
        # ETL
        data_t_prep = mod1.prepare_data(data_t)
        
        # Train the model object
        mod1.model = mod1.train_model(data_t_prep)
      
        
        #############################################
        # Operation
        #############################################
        
        # Predict
        pred_t = mod1.predict(data_t_prep)
                
        # Set up automation object
        case_manager = self.p.Automation(self.automation_settings)
        
        # re_prioritize cases
        prioritized_cases = case_manager.prioritize(cases=data_t_prep, 
                          predictions=pred_t)
        
        """ here some process automation is implemented """
        print(prioritized_cases)
        
        
############################################
# Test an experiment:
############################################
    

Doe_factors = {"Factor1":[0,1],
                    "Factor2":[0,1]}

p1 = Experiment(Doe_factors, 36)

p1.run_experiment()

p1.save_data("/files/run_i.npy")


"""
The experiment class should hold everything related to an experiment;
A simulation class should hold everything related to a simulation
A model training class should hold everything related to model training

https://www.w3schools.com/python/python_classes.asp

"""

############################################



