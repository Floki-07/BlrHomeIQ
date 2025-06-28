from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form values
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])
    bhk = int(request.form['BHK'])

    # Create input DataFrame (match training structure)
    input_data = pd.DataFrame([{
        'location': location,
        'total_sqft': total_sqft,
        'bath': bath,
        'balcony': balcony,
        'BHK': bhk
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]
    predicted_price = round(prediction, 2)

    if predicted_price <= 100:
         price_str = f"₹{predicted_price} Lakhs"
    else:
        price_str = f"₹{round(predicted_price / 100, 2)} Crores"

    return render_template('result.html', price=price_str)

if __name__ == '__main__':
    app.run(debug=True)
