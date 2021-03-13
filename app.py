import numpy as np
from flask import Flask, request , jsonify, render_template
import pickle


app = Flask(__name__)
model_stroke = pickle.load(open('model_rf.pkl','rb'))
model_crop = pickle.load(open("model_crop.pkl","rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/stroke')
def stroke():
    return render_template('stroke.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_stroke.predict(final_features)
    output = prediction[0]
    
    if output == 1 :
        return render_template('stroke.html', prediction_text="Please See a Doctor!! You have an high chance of getting a stroke")
    
    else:

        return render_template('stroke.html', prediction_text="Be happy! You have lesss probability of occurance of stroke")

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/predictcrop',methods=['POST'])
def predictcrop():
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_crop.predict(final_features)
    output = prediction[0]

    return render_template('crop.html', prediction_text="The crop which you can grow is {}".format(output))
           
if __name__ == "__main__":
    app.run(debug=True)
#if __name__=="__main__":
   # app.run(host = '0.0.0.0',port=8080)