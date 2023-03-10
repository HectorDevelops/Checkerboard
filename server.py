from flask import Flask, render_template
# importing the math library to apply in the route return
import math

app = Flask(__name__)

@app.route('/')
def checkerboard():
    # applying math.floor to get whole number for checker-box
    return render_template ("checkerboard.html", x=math.floor(8/2), y=math.floor(8/2), color1="#FFFFFF", color2="#000000")

@app.route('/<int:x>')
def customize(x):
    # applying math.floor to get whole number for checker-box
    return render_template ("checkerboard.html", x=math.floor(x/2), y=math.floor(8/2), color1="#FFFFFF", color2="#000000")

@app.route('/<int:x>/<int:y>')
def customMade(x, y):
    # applying math.floor to get whole number for checker-box
    return render_template ("checkerboard.html", x=math.floor(x/2), y=math.floor(y/2), color1="#FFFFFF", color2="#000000")

@app.route('/<int:x>/<int:y>/<color1>')
def colorCustom(x, y, color1):
    # applying math.floor to get whole number for checker-box
    return render_template ("checkerboard.html", x=math.floor(x/2), y=math.floor(y/2), color1=color1, color2=000000)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colorComplete(x, y, color1, color2):
    # applying math.floor to get whole number for checker-box
    return render_template ("checkerboard.html", x=math.floor(x/2), y=math.floor(y/2), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
