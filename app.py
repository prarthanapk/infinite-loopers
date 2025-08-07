from flask import Flask, render_template
import subprocess
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/wave")
def wave():
    subprocess.Popen(["python", "gesture_control.py"])
    return render_template("running.html",
                           title="Gesture Control Running",
                           emoji="🖐",
                           message="Gesture Control Running...")

@app.route("/type_scream")
def type_scream():
    subprocess.Popen(["python", "scream_to_type.py"], cwd=os.getcwd())
    return "🎤 Scream-to-Type Running..."
    # If you want to render a template instead, comment above and uncomment below
    # return render_template("scream.html")

@app.route("/useless_math")
def useless_math():
    # If you want to both run a script and show results, do it here.
    # subprocess.Popen(["python", "useless_math.py"], cwd=os.getcwd())
    results = []
    for _ in range(10):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        op = random.choice(["+", "-", "*", "/", "**"])
        try:
            result = eval(f"{a} {op} {b}")
        except Exception:
            result = "🤯 too useless to compute"
        results.append(f"{a} {op} {b} = {result}")
    return render_template("useless_math.html", results=results)

@app.route("/self_love")
def compliment():
    subprocess.Popen(["python", "compliment_ai.py"], cwd=os.getcwd())
    return "💗 Compliment AI Running..."
    # Or, if you want to show a template:
    # return render_template("self_love.html")

if __name__ == "__main__":
    app.run(debug=True)
