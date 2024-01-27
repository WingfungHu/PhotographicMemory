from flask import Flask, render_template, request

app = Flask(__name__)

# global coutner
# counter = 0

@app.route("/")
def start():
    # global counter

    # counter = 0
    # print(counter)
    return render_template('homepage.html')

@app.route("/process_text", methods=['GET', 'POST'])
def move_forward():
    # global counter
    # print(counter)
    # counter += 1
    text = request.form['input_image_url']
    return render_template('homepage.html', display_input=text)
    # if counter % 2 == 0:   
    #     return render_template('homepage.html', display_input=text)
    # else: 
    #     return render_template('homepage.html', forward_message="forward_message", display_input=text)