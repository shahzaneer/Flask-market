from flask import Flask

# ! WEB Server gateway interface instance of flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<a href=""> Hello, World!</a>"

@app.route("/cui")
def hello_CUI():
    return "<a href=""> Hello, CUI!</a>"

@app.route("/gcu")
def hello_GCU():
    return "<a href=""> Hello, GCU!</a>"

@app.route("/tedx")
def hello_tedx():
    return "<a href=""> Hello, TEDx!</a>"


if __name__ == '__main__':
    app.run(debug=True)
        