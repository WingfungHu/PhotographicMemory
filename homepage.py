from flask import Flask, render_template, request, app
from backend import Backend

app = Flask(__name__)
global backend_object
# global coutner
# counter = 0

@app.route("/")
def start():
    # global counter
    app.logger.debug('A value for debugging')
    global backend_object
    backend_object = Backend()
    app.logger.debug(backend_object.print_current_state())
    # counter = 0
    # print(counter)
    return render_template('homepage.html')

@app.route("/upload_image", methods=['GET', 'POST'])
def move_forward():
    global backend_object
    # global counter
    # print(counter)
    # counter += 1
    input_url = request.form['input_image_url']
    backend_object.upload_picture(input_url)
    app.logger.debug(backend_object.print_current_state())

    return render_template('homepage.html', display_input=input_url)
    # if counter % 2 == 0:   
    #     return render_template('homepage.html', display_input=text)
    # else: 
    #     return render_template('homepage.html', forward_message="forward_message", display_input=text)