#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

# file = open("mo
# del.pkl","rb")
file = open("model.pkl", "rb")

gbc = pickle.load(file)


app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/performance')
def performance():
	return render_template('performance.html')

@app.route('/chart')
def chart():
	return render_template('chart.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	

@app.route('/index')
def index():
    return render_template('index.html')



@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe///-
        print(y_pred)
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        print(y_pro_phishing)
        print(y_pro_non_phishing)
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('result.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template("result.html", xx =-1)


if __name__ == "__main__":
    app.run(debug=True)