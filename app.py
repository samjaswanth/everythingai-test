import numpy as np
from flask import Flask, request , jsonify, render_template
import pickle


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)
#if __name__=="__main__":
   # app.run(host = '0.0.0.0',port=8080)