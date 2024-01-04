from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np
import sklearn
import os,sys



app = Flask(__name__)


#@app.route("/")
#def index():
    #return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():

    temparature = float(request.form['temparature'])
    humidity = float(request.form['humidity'])
    moisture = float(request.form['moisture'])
    oiltype = float(request.form['oiltype'])
    croptype = float(request.form['croptype'])
    nitrogen = float(request.form['nitrogen'])
    potassium = float(request.form['potassium'])
    phosphorous = float(request.form['phosphorous'])
   

    X = np.array([['temparature', 'humidity', 'moisture', 'oiltype', 'croptype',
       'nitrogen', 'potassium', 'phosphorous']])


    model_path = r'C:\Users\aswin\OneDrive\Documents\Data Science\Machine Learning Project\Fertilizer-Predict\model.pkl'

    model = joblib.load(model_path)

    Y_pred = model.predict(X)

    return jsonify({'Prediction': float(Y_pred)})


if __name__ == "__main__":
    app.run(debug=True, port=500)
    