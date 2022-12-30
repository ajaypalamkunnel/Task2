from flask import Flask,request
from helpers import ran

app = Flask(__name__)

@app.route("/")
def homepage():
    return "How are you?"

@app.route("/random")
def data():
    mini = request.args.get("mini")
    maxi = request.args.get("maxi")
    if not mini and maxi:
        return {"ok":"error","error":"no data provided"}
    ranlist =ran(minimum=int(mini),maximum=int(maxi))
    print(ranlist)
    return str(ranlist)