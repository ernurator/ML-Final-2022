import os
import uuid

from flask import request, Flask, render_template

import numpy as np
from tensorflow import keras
from PIL import Image

app = Flask(__name__)

print("something)")

# Classes of trafic signs
IMAGE_CLASSES = {
    0: 'Speed limit [20]',
    1: 'Speed limit [30]',
    2: 'Speed limit [50]',
    3: 'Speed limit [60]',
    4: 'Speed limit [70]',
    5: 'Speed limit [80]',
    6: 'End of speed limit [80]',
    7: 'Speed limit [100]',
    8: 'Speed limit [120]',
    9: 'No passing',
    10: 'No trucks passing',
    11: 'Right-of-way at intersection',
    12: 'Priority road',
    13: 'Yield',
    14: 'Stop',
    15: 'No vehicles',
    16: 'No trucks',
    17: 'No entry',
    18: 'General caution',
    19: 'Dangerous curve left',
    20: 'Dangerous curve right',
    21: 'Double curve',
    22: 'Bumpy road',
    23: 'Slippery road',
    24: 'Road narrows on the right',
    25: 'Road work',
    26: 'Traffic signals',
    27: 'Pedestrians',
    28: 'Children crossing',
    29: 'Bicycles crossing',
    30: 'Beware of ice/snow',
    31: 'Wild animals crossing',
    32: 'Speed and passing limits end',
    33: 'Turn right ahead',
    34: 'Turn left ahead',
    35: 'Ahead only',
    36: 'Go straight or right',
    37: 'Go straight or left',
    38: 'Keep right',
    39: 'Keep left',
    40: 'Roundabout',
    41: 'End of no passing',
    42: 'End of no passing trucks'
}


def predict_image(img):
    image = Image.open(img).convert('RGB')
    image = image.resize((60, 60))
    X_test = np.array(image).reshape((1, 60, 60, 3))
    model = keras.models.load_model('./model.20-0.02.h5')
    predicted_labels_score = model.predict(X_test)
    predicted_label = np.argmax(predicted_labels_score, axis=1)[0]
    return IMAGE_CLASSES[predicted_label]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file_path = str(uuid.uuid4())
        request.files['file'].save(file_path)
        result = predict_image(file_path)
        os.remove(file_path)
        return 'Predicted Traffic🚦Sign is: ' + result
    return None


if __name__ == '__main__':
    app.run()
