from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import cv2
import os

model = tf.keras.models.load_model('transfer_learning_model.keras', compile=False, custom_objects={'input_shape': (224,224,3)})
app = Flask(__name__, template_folder='page')

folder = os.path.join('static', 'upload')
os.makedirs(folder, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_path = None

    if request.method == 'POST':
        if 'image' not in request.files:
            result = 'No image uploaded'
        else:
            file = request.files['image']
            if file.filename == '':
                result = 'No file selected'
            else:
                filename = secure_filename(file.filename)
                saved_path = os.path.join(folder, filename)
                file.save(saved_path)

                #preprocessing
                img = cv2.imread(saved_path)
                img = cv2.resize(img, (224, 224))
                img = img / 255.0
                img = np.expand_dims(img, axis=0)

                #predict
                pred = model.predict(img)
                result = 'Edible' if pred[0][0] < 0.5 else 'Poisonous'

                image_path = url_for('static', filename='upload/' + filename)

    return render_template('index.html', result=result, image_path=image_path)

@app.route('/refresh', methods=['POST'])
def refresh():
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.exists(path):
            os.remove(path)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)