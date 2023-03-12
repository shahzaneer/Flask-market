from flask import Flask , redirect, url_for, render_template, request

#! Integrating HTML with Flask
#! HTTP verbs -> GET and POST

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if(score >= 50):
        res = "pass"
    else:
        res = "fail"    
    # return "The student has passed with score = " + str(score)
    return render_template("result.html", result = res)

@app.route("/fail/<int:score>")
def fail(score):
    return "The student has failed with score = " + str(score)


#! Checker 
@app.route("/result/<int:marks>")
def result(marks):
    if(marks>=50):
        result = "success"
    else:
        result = "fail"

    return redirect(url_for(result,score=marks))        



#! Checker from URL
@app.route("/submit" , methods=["POST","GET"])
def submit():
    totalScore = 0
    if request.method == "POST":
        pf = int(request.form["pf"])
        oop = int(request.form["oop"])
        dsa = int(request.form["dsa"])
        web = int(request.form["web"])
        totalScore = (pf + oop + dsa + web) / 4

    res = ""
    if(totalScore >=50):
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res,score=totalScore))            
        

    


if __name__ == '__main__':
    app.run(debug=True)
    