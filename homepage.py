from flask import Flask
from flask import render_template

app = Flask(__name__)

global coutner
counter = 0

@app.route("/")
def start():
    global counter

    # counter = 0
    print(counter)
    return render_template('homepage.html')

@app.route("/change/", methods=['POST'])
def move_forward():
    global counter
    print(counter)
    counter += 1
    if counter % 2 == 0:   
        return render_template('homepage.html')
    else: 
        return render_template('homepage.html', forward_message="forward_message")