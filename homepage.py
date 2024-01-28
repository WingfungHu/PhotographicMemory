from flask import Flask, render_template, request, app, redirect, url_for, session, send_from_directory
from backend import Backend
import jsonify
import sys
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
global backend_object
# global coutner
# counter = 0
image_storage = []
text_storage = []

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GETgit', 'POST'])
def home():
    app.logger.debug('A value for debugging')
    global backend_object
    backend_object = Backend()
    app.logger.debug(backend_object.print_current_state())
    if request.method == 'POST':
        if 'image-upload' in request.files:
            file = request.files['image-upload']
            if file and allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                return render_template('homepage.html', uploaded=True, filename=file.filename)

    return render_template('homepage.html', uploaded=False)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# @app.route("/")
# def start():
#     # global counter
#     app.logger.debug('A value for debugging')
#     global backend_object
#     backend_object = Backend()
#     app.logger.debug(backend_object.print_current_state())
#     # counter = 0
#     # print(counter)
#     return render_template('homepage.html')


@app.route("/upload_image", methods=['GET', 'POST'])
def move_forward():
    global backend_object

    if request.method == 'POST':
        data = request.get_json()  # retrieve the data sent from JavaScript

        # input_url = request.form['input_image_url']
        app.logger.debug(data)
        input_url = data["imageUrl"]

        # input_url = "placeholder"
        image_storage.append(input_url)
        generate_response = backend_object.upload_picture(input_url)
        app.logger.debug(backend_object.print_current_state())
        app.logger.debug("Finish Upload picture")

        session['display_input'] = image_storage
        session['updated'] = 'display_input'
        return generate_response["message"]
        # return redirect(url_for('display'))
    return render_template('homepage.html')

    # backend_object.upload_picture(input_url)
    # app.logger.debug(backend_object.print_current_state())


@app.route("/display")
def display():
    display_input = session.get('display_input', None)
    display_text = session.get('display_text', None)
    updated = session.pop('updated', None)
    if updated == 'display_input':
        session.pop('display_input', None)
    else:
        session.pop('display_text', None)
    return render_template('homepage.html', display_input=', '.join(display_input) if display_input else None,
                           display_text=display_text if display_text else None)


@app.route("/send_text", methods=['GET', 'POST'])
def send_text():
    if request.method == 'POST':
        input_text = request.form['input_text']
        text_storage.append(input_text)
        session['display_text'] = text_storage
        session['updated'] = 'display_text'
        return redirect(url_for('display'))
    return render_template('homepage.html')


@app.route("/process_user_input_to_chatbot", methods=['GET', 'POST'])
def process_user_input_to_chatbot():
    global backend_object

    data = request.get_json()  # retrieve the data sent from JavaScript
    # process the data using Python code
    # result = data['value'] * 2
    print("User INput: ", data, file=sys.stdout)
    result = backend_object.execute_chatbot_input(data)
    return result
    return jsonify(result=result)  # return the result to JavaScript
    if request.method == 'POST':
        input_text = request.form['input_text']
        text_storage.append(input_text)
        session['display_text'] = text_storage
        session['updated'] = 'display_text'
        return redirect(url_for('display'))
    return render_template('homepage.html')
