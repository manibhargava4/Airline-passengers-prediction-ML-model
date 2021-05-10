from keras.models import load_model
from flask import Flask, render_template, request, url_for, redirect
import numpy as np

app = Flask("passmodelapp")

model = load_model("pass_model.h5")

@app.route('/')
def hello_world():
    return render_template("airline.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[[int(x) for x in request.form.values()]]
    print(int_features)
    output=model.predict(int_features)
    prediction = round(output[0][0])

    if prediction == 0:
        return render_template('airline.html',pred='Customer is either neutral/dissatisfied with the services provided.')
    else:
        return render_template('airline.html',pred='Customer is satisfied with the services provided.')


app.run(host="172.17.0.2", port=8080)






