from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('bmi_checker.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def home():
    #gender_female=0
    gender_male=request.form['gender']
    if(gender_male=='Male'):
        gender_male=1
        #gender_female=0
    else:
        #gender_female=1
        gender_male=0
    height=request.form['height']
    weight=request.form['weight']
    prediction=model.predict([[gender_male,height,weight,]])
    output=prediction[0]
    return render_template('index.html',data=output)

if __name__ == '__main__':
    app.run(debug=True)
