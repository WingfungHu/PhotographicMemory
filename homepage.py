from flask import Flask, render_template, request, app, redirect, url_for, session
from backend import Backend

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
global backend_object
# global coutner
# counter = 0
image_storage = []

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
    if request.method == 'POST':
        input_url = request.form['input_image_url']
        image_storage.append(input_url)
        session['display_input'] = image_storage
        return redirect(url_for('display'))
    return render_template('homepage.html')

    # backend_object.upload_picture(input_url)
    # app.logger.debug(backend_object.print_current_state())

@app.route("/display")
def display():
    display_input = session.get('display_input', None)
    session.pop('display_input', None)
    return render_template('homepage.html', display_input=', '.join(display_input) if display_input else None)