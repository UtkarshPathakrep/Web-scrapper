from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def get_post():
    return jsonify({"Hello":"World"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8082,debug=True)