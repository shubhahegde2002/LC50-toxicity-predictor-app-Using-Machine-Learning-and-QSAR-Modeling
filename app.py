from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

# Initalise the Flask app
app = Flask(__name__)

filename='rf.sav'
loaded_model = pickle.load(open(filename, 'rb'))

cols = ['CIC0', 'SM1_Dz(Z)', 'GATS1i', ' NdsCH', 'NdssC', 'MLOGP']
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    final1=final.reshape(1,-1)
    prediction = loaded_model.predict(final1)[0]
    return render_template('home.html',pred='Expected LC50 value will be {0:.2f}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = loaded_model.predict(data_unseen)
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)