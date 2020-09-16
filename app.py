from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html");

@app.route('/color/photo',methods=['post'])
def color():
    return "hi";

if __name__ == "__main__":
    app.run(debug=True)
