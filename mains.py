from flask import Flask,render_template,request

from utils import DiebeticOrNot

app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('Diebetes Prediction..')
    return render_template('index.html')

@app.route('/predict_diebetes',methods=['GET','POST'])
def get_diebetes_info():
    
    if request.method == 'GET':
        print('GET Method...')
        
        # data = request.form
        
        # Glucose = eval(data['Glucose'])
        # BloodPressure = eval(data['BloodPressure'])
        # SkinThickness = eval(data['SkinThickness'])
        # Insulin = eval(data['Insulin'])
        # BMI = eval(data['BMI'])
        # DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFunction'])
        # Age = eval(data['Age'])
        
        # return f'Patient is Diebetic...'
        
        Glucose = eval(request.args.get('Glucose'))
        BloodPressure = eval(request.args.get('BloodPressure'))
        SkinThickness = eval(request.args.get('SkinThickness'))
        Insulin = eval(request.args.get('Insulin'))
        BMI = eval(request.args.get('BMI'))
        DiabetesPedigreeFunction = eval(request.args.get('DiabetesPedigreeFunction'))
        Age = eval(request.args.get('Age'))
        
        print('Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age :',Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        
        diebetic = DiebeticOrNot(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        
        yes_no = diebetic.get_predicted_diebetes()
        
        if yes_no == 1:
            
            yes_no = 'Patient is Diebetic..'
            
        else :
            
            yes_no = 'Patient is NOT Diebetic..'
            
        return render_template('index.html',prediction = yes_no)
        
           
    # else :
        
    #     print('POST Method...')
        
    #     data = request.form
        
    #     Glucose = eval(data['Glucose'])
    #     BloodPressure = eval(data['BloodPressure'])
    #     SkinThickness = eval(data['SkinThickness'])
    #     Insulin = eval(data['Insulin'])
    #     BMI = eval(data['BMI'])
    #     DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFunction'])
    #     Age = eval(data['Age'])
        
    #     return f'Patient is NOT Diebetic...'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()
    
        