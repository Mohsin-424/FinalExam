from flask import Flask, request, jsonify
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

app = Flask(__name__)

# Create a simple linear regression model for demonstration
def create_model():
    # Create a simple dataset
    X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
    
    # Split into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model to a file
    joblib.dump(model, 'linear_regression_model.pkl')
    return model

# Load the model
model = create_model()

@app.route('/')
def home():
    return "Welcome to the Linear Regression API. Use /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Get the input features from the POST request
    try:
        input_features = np.array(data['input_features']).reshape(1, -1)
    except KeyError:
        return jsonify({"error": "No input features provided"}), 400

    # Predict the target variable
    prediction = model.predict(input_features)
    
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
