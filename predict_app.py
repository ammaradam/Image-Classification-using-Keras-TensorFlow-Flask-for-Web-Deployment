# Import all necessary dependencies
import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

# Create instance of Flask class
app = Flask(__name__)

# Get_model function: load trained and saved model to memory
def get_model():
    # Define variable model as Global to make it accessible throughout the code
    global model
    
    # Load model using pre-defined Keras function
    model = load_model('VGG16_cats_and_dogs.h5')
    print(" * Model loaded!")
    
# Convert format of input image to suitable format for our Keras model
def preprocess_image(image, target_size):
    # Check if image is in RGB format. If not, convert to RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize image to target size to fit our model
    image = image.resize(target_size)
    
    # Convert PIL image format to numpy array
    image = img_to_array(image)
    
    # Expand shape of array by inserting new axis
    image = np.expand_dims(image, axis=0)
    
    # Send pre-processed image
    return image

# Display current status
print(" * Loading Keras model...")

# Load model into memory once
get_model()

# Decorator defining URL endpoint to implement following module, allow HTTP POST request to endpoint
@app.route("/predict", methods=["POST"])
# Define what to do when POST request is received
def predict():
    # Access info sent to '/predict' endpoint, in JSON format 
    message = request.get_json(force=True)
    
    # Extract key-value pair with key named 'image', expecting base64 encoded image
    encoded = message['image']
    
    # Decode the encoded image data
    decoded = base64.b64decode(encoded)
    
    # Set to instance of PIL image, open decoded Image file
    image = Image.open(io.BytesIO(decoded))
    
    # Pre-process image
    processed_image = preprocess_image(image, target_size=(224, 224))
    
    # Expect np array from predict function, convert np array to list
    prediction = model.predict(processed_image).tolist()

    # Response returned by Flask to web app
    response = {
        # Return as dictionary with key 'prediction', value 'dog' and 'cat' prediction
        'prediction': {
            'dog': prediction[0][0],
            'cat': prediction[0][1]
        }
    }
    # Convert dictionary to JSON
    return jsonify(response)
