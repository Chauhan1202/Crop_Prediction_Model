import numpy as np
import pickle
from flask import Flask, request, render_template

# Create application
app = Flask(__name__)

# Load machine learning model
model = pickle.load(open('model.pkl', 'rb'))

# Bind home function to URL
@app.route('/')
def home():
    return render_template('crop.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
 
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
 
    output = prediction

 
    # Check the output values and retrieve the result with html tag based on the value
 
    if output == 'Apple':
        return render_template('crop.html',result = 'The Soil is suitable for Apple cultivation')

    elif output == 'Banana':
        return render_template('crop.html', result = 'The Soil is suitable for Banana cultivation')
    
    elif output == 'Blackgram':
        return render_template('crop.html', result = 'The Soil is suitable for Blackgram cultivation')
    
    elif output == 'ChickPea':
        return render_template('crop.html', result = 'The Soil is suitable for ChickPea cultivation')
    
    elif output == 'Coconut':
        return render_template('crop.html', result = 'The Soil is suitable for Coconut cultivation')
    
    elif output == 'Coffee':
        return render_template('crop.html', result = 'The Soil is suitable for Coffee cultivation')
    
    elif output == 'Cotton':
        return render_template('crop.html', result = 'The Soil is suitable for Cotton cultivation')
    
    elif output == 'Grapes':
        return render_template('crop.html', result = 'The Soil is suitable for Grapes cultivation')
    
    elif output == 'Jute':
        return render_template('crop.html', result = 'The Soil is suitable for Jute cultivation')
    
    elif output == 'KidneyBeans':
        return render_template('crop.html', result = 'The Soil is suitable for KidneyBeans cultivation')
    
    elif output == 'Lentil':
        return render_template('crop.html', result = 'The Soil is suitable for Lentil cultivation')
    
    elif output == 'Maize':
        return render_template('crop.html', result = 'The Soil is suitable for Maize cultivation')
    
    elif output == 'Mango':
        return render_template('crop.html', result = 'The Soil is suitable for Mango cultivation')
    
    elif output == 'MothBeans':
        return render_template('crop.html', result = 'The Soil is suitable for MothBeans cultivation')
    
    elif output == 'MungBean':
        return render_template('crop.html', result = 'The Soil is suitable for MungBean cultivation')
    
    elif output == 'Muskmelon':
        return render_template('crop.html', result = 'The Soil is suitable for Muskmelon cultivation')
    
    elif output == 'Orange':
        return render_template('crop.html', result = 'The Soil is suitable for Orange cultivation')
    
    elif output == 'Papaya':
        return render_template('crop.html', result = 'The Soil is suitable for Papaya cultivation')
    
    elif output == 'PigeonPeas':
        return render_template('crop.html', result = 'The Soil is suitable for PigeonPeas cultivation')
    
    elif output == 'Pomegranate':
        return render_template('crop.html', result = 'The Soil is suitable for Pomegranate cultivation')
    
    elif output == 'Rice':
        return render_template('crop.html', result = 'The Soil is suitable for Rice cultivation')
    
    elif output == 'Watermelon':
        return render_template('crop.html', result = 'The Soil is suitable for Watermelon cultivation')
    
if __name__ == '__main__':
#Run the application
    app.run()