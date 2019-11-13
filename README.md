# Image Classification using Keras TensorFlow Flask for Web Deployment

This project is a compilation and derivation from "Deploy Keras neural network to Flask web service" videos by deeplizard 
(Source: https://www.youtube.com/channel/UC4UJ26WkceqONNF5S26OiVw)


## Overview
One simple approach to deploy our trained Neural Network model into production. This repo uses combination of following applications:
- **Web Service**: Flask
- **NN Library**: Keras
- **Backend**: Theano / Tensorflow / CNTK
- **Web Backend Language**: Python


This project aims to achieve following objectives:
1) To build a Flask app
2) To send and receive data with Flask
3) To build a front end web app
4) To host VGG16 model with Flask
5) To build a web app to send images to VGG16

## Getting Started
### Pre-requisites
- Pillow
- Keras
- Theano / Tensorflow / CNTK
- Flask

Install the pre-requisites:
```
pip install -r requirements.txt
```

### Installation
```
git clone https://github.com/ammaradam/Image-Classification-using-Keras-TensorFlow-Flask-for-Web-Deployment
cd flask_apps
```

### Deployment
1) Set Flask app directory in command prompt
```
set FLASK_APP=predict_app.py
```
2) Run Flask app server in command prompt
```
flask run --host=0.0.0.0
```
3) Access from browser on local server
- Open any browser and access the webpage
```
http://127.0.0.1:5000/static/predict.html
```
