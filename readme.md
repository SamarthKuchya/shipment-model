# Shipment Prediction Web Application

This Flask-based web application predicts whether a shipment will be successful or not based on input parameters such as origin, destination, vehicle type, distance, weather conditions, and traffic conditions. The prediction model uses a Decision Tree classifier, which is suitable for handling data with an if-else pattern.

---

## Features
- User-friendly interface to input shipment details.
- Predicts shipment success based on historical data.
- Handles invalid or missing input values gracefully.

---

## Installation and Setup

### Prerequisites
1. Python 3.7 or higher.
2. Required Python libraries (listed in `requirements.txt`).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shipment-prediction.git
   cd shipment-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://localhost:5000
   ```

---

## Usage
1. Open the application in your browser (`localhost:5000`).
2. Enter the following details:
   - **Origin**: Select the shipment's starting location.
   - **Destination**: Select the shipment's destination.
   - **Vehicle Type**: Choose the type of vehicle used for the shipment.
   - **Distance (km)**: Enter the distance to be covered in kilometers.
   - **Weather Conditions**: Select the current weather conditions.
   - **Traffic Conditions**: Select the traffic conditions.
3. Click on the "Predict" button to see whether the shipment will be successful or not.

---

## How It Works
1. **Input Data**: User inputs shipment details in the form.
2. **Data Encoding**: Inputs are encoded into numerical values using predefined dictionaries.
3. **Feature Vector**: A feature vector is created from the encoded inputs.
4. **Prediction**: The feature vector is passed to a Decision Tree model to make a prediction.
5. **Output**: The result (Yes/No) is displayed on the webpage.

---

## Model Information
- **Algorithm**: Decision Tree Classifier.
- **Reason for Selection**: Decision Trees handle data with an if-else pattern, making them suitable for this dataset.

---

## Project Structure
- `app.py`: Main application file.
- `shipments.pkl`: Pre-trained Decision Tree model.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: List of dependencies.

---

## Contribution
Feel free to fork this repository and contribute to its development by submitting pull requests. Suggestions and feedback are always welcome!

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
Special thanks to all contributors and users who have helped improve this project.

