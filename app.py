import numpy as np
from flask import Flask, request , jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model_rf.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/stroke')
def stroke():
    return render_template('stroke.html')
@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    
    if output == 1 :
        return render_template('stroke.html', prediction_text="Please See a Doctor!! You have an high chance of getting a stroke")
    
    else:

        return render_template('stroke.html', prediction_text="Be happy! You have lesss probability of occurance of stroke")
           
if __name__ == "__main__":
    app.run(debug=True)
#if __name__=="__main__":
   # app.run(host = '0.0.0.0',port=8080)