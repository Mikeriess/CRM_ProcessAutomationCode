# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:29:53 2021

@author: Mike
"""


class Automation:
    def __init__(self, priorization_scheme):
                
        self.priorization_scheme = priorization_scheme
        
    def prioritize(self, cases, predictions):
        
        if self.priorization_scheme == "FIFO":
            print("performing FIFO reprioritization")
            cases_repriotized = cases
        
        if self.priorization_scheme == "LIFO":
            print("performing LIFO reprioritization")
            cases_repriotized = cases
            
        if self.priorization_scheme == "PPM":
            print("performing RT model-based (PPM) reprioritization")
            cases_repriotized = cases
            

        return cases_repriotized
    
    
