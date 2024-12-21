# Import the required libraries
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model from the saved .pkl file
with open('shipments.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route to Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to Prediction page
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the form
        origin = request.form.get('Origin')
        destination = request.form.get('Destination')
        vehicle_type = request.form.get('Vehicle Type')
        distance = request.form.get('Distance (km)')
        weather_conditions = request.form.get('Weather Conditions')
        traffic_conditions = request.form.get('Traffic Conditions')

        # Convert the input data to the required format for prediction
        weather_dict = {'Clear':0,'Fog':1,'Rain':2,'Storm':3}
        traffic_dict = {'Heavy': 0, 'Light': 1, 'Moderate': 2}
        origin_dict = {'Ahmedabad': 0,
                       'Bangalore': 1,
                       'Chennai': 2,
                       'Delhi': 3,
                       'Hyderabad': 4,
                       'Jaipur': 5,
                       'Kolkata': 6,
                       'Lucknow': 7,
                       'Mumbai': 8,
                       'Pune': 9}
        veh_dict={'Container': 0, 'Lorry': 1, 'Trailer': 2, 'Truck': 3}


        weather_encoded = weather_dict.get(weather_conditions, -1)  # Default to -1 if invalid weather condition
        traffic_encoded = traffic_dict.get(traffic_conditions, -1)  # Default to -1 if invalid traffic condition
        origin_encoded = origin_dict.get(origin, -1)
        destination_encoded = origin_dict.get(destination, -1)
        vehicle_type = veh_dict.get(vehicle_type, -1)

        # Create a feature vector for prediction
        features = np.array([[origin_encoded, destination_encoded, vehicle_type, distance, weather_encoded, traffic_encoded]])

        # Send the feature vector to the model for prediction
        prediction = model.predict(features)
        if(prediction==0):
            prediction='No'
        else:
            prediction='Yes'

        # Display the prediction on the webpage
        return render_template('index.html', prediction=prediction, origin=origin, destination=destination)

    # Handle exceptions
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
