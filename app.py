import numpy as np
from flask import Flask,request,render_template
import pickle 
from joblib import load
app = Flask(__name__)
model = pickle.load(open('deci.p','rb'))

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test=[[float(x) for x in request.form.values()]]
    print(x_test)
    sc=load('scalar.save')
    prediction=model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[0]
    if(output==0):
        pred="YOUR RISK FACTOR IS LOW"
    else:
        pred="YOUR RISK FACTOR IS HIGH"
    
    return render_template('front.html',prediction_text='User : {}'.format(pred))

if __name__=="__main__":
    app.run(debug=True)
    