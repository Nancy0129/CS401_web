import pickle
import numpy as np
from flask import Flask, request, jsonify,render_template,send_file
import os, time

app = Flask(__name__)

with open('ML.pickle','rb') as f:
    app.model=pickle.load(f)
    app.t=pickle.load(f)
    app.v=pickle.load(f)

app.CV = pickle.load(open("CV.pickle", "rb"))
app.TF = pickle.load(open("TF.pickle", "rb"))

@app.route("/api/american")
def input_text():
    return render_template("input.html")

@app.route("/api/american/out", methods=["POST"])
def prediction():
    text=request.form['in_text']
    textCV=app.CV.transform(np.array([text]))
    textTF=app.TF.transform(textCV)
    pre=app.model.predict(textTF)
    app.json={'is_american':str(pre[0]),'version':app.v,'model_date':app.t}
    return render_template("out.html",in_text=text,pre=pre[0],
                           version=app.v, model_date=app.t)


@app.route("/api/american/download")
def download_json():
    with open("response.out", "w") as f:
        f.write(str(app.json))
    
    return send_file("response.out",as_attachment=True)