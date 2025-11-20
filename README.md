## Preview
![Image](https://github.com/user-attachments/assets/ec73ed42-cc9d-4258-82f4-de3ae9aeee1f)

## Description
Fungi Image Classification using CNN Model and Transfer Learning (MobileNet2.0). Models classify in 2 classes (edible or poisonous fungi), the Transfer Learning model implemented to web due to high accuracy. The goal is to create a simple website to classify fungi image whether it's edible or not.
<br>
## Dataset
This project utilized dataset from: <br>
https://www.kaggle.com/datasets/marcosvolpato/edible-and-poisonous-fungi
<br>
## Installation
⚠️ Important:<br>
If you are using TensorFlow 2.17+ or Keras 3.6+ and encounter issue double tensor, install these versions:
```
pip install tensorflow==2.15.0 keras==3.3.3
```
## Run The Application
Run the Flask Server:
```
flask --app main.py --debug run
```
