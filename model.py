# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:25:44 2021

@author: Mike
"""



class model:
    def __init__(self, modelformat, settings):
        
        self.modelformat = modelformat #"model settings"
        self.settings = settings # HPO settings
        self.model = "initial_model_object"
        
    def prepare_data(self, input_data):
        
        print("preparing data for: " + self.modelformat)
        
        output_data = input_data
        
        return output_data
    
    def train_model(self, input_data):
        
        print("training:" + self.modelformat +", with: " + self.settings)
        
        model = "trained model"
        
        return model
    
    def predict(self, input_data):
        
        print("predicting from "+ self.model)
        
        output_data = input_data
        
        return output_data


#mod1 = model("dataset","hpo settings 1")

#mod1.prepare_data()

#mod1.train_model()