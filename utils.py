import pickle
import json 
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import config 

class DiebeticOrNot():
    
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f :
            self.logistic_model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r' )as f :
            self.save_data = json.load(f)
            
            self.column_names = self.save_data['column_names']
            
    def get_predicted_diebetes(self):
        
        self.load_models()
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age
        
        print('Array is :',array)
        
        yes_no = self.logistic_model.predict([array])[0]
        
        return yes_no
    
if  __name__ == '__main__':
    
    Glucose = 148.000
    BloodPressure = 50.000
    SkinThickness = 35.000
    Insulin = 0.000
    BMI = 33.600
    DiabetesPedigreeFunction = 0.627
    Age = 50.000
    
    diebetic = DiebeticOrNot(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    
    yes_no = diebetic.get_predicted_diebetes()
    
    if yes_no == 1 :
        
        print('Diebetic...')
        
    else :
        
        print('Not Diebetic...') 
                   