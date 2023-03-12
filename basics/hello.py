from flask import Flask , redirect, url_for;

#! Dynamically building URLS by rules and URL Binding

app = Flask(__name__)

@app.route("/")
def shah():
    return "Shah taking on Flask"

@app.route("/success/<int:score>")
def success(score):
    return "The student has passed with score = " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The student has failed with score = " + str(score)

@app.route("/result/<int:marks>")
def result(marks):
    if(marks>=50):
        result = "success"
    else:
        result = "fail"

    return redirect(url_for(result,score=marks))        


if __name__ == '__main__':
    app.run(debug=True)
    