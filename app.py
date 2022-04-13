import os
from flask import Flask,request


app = Flask(__name__)


@app.route("/canary/web",methods=['GET','POST'])
def web_canary():
    print(request.get_json())
    return "Hello World"

PORT = os.getenv('PORT') or 5000

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=PORT)