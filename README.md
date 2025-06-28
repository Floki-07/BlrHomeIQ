

# 🏡 BLRHomeIQ

**BLRHomeIQ** is a web-based house price prediction app specifically designed for Bangalore. Using a trained **Linear Regression model**, the app estimates property prices based on location, size (in square feet), number of bedrooms, and bathrooms. 

---

## 🚀 Features

* 🧠 Predict housing prices in Bangalore
* 🏙️ Location-based and feature-driven predictions
* 💻 Simple HTML form for user input
* 🔁 Real-time predictions using Flask backend
* 📉 Trained using Linear Regression on cleaned data

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS
* **Backend**: Python, Flask
* **ML Model**: Scikit-learn (Linear Regression)
* **Data Handling**: Pandas, NumPy

---

## 🧠 How It Works

1. The user enters house features (location, sqft, BHK, bath) via an HTML form.
2. The form sends the data to a Flask backend using a POST request.
3. The backend uses a trained Linear Regression model to predict the price.
4. The prediction is returned and shown on the webpage.

---

## 📁 Project Structure

```
BLRHomeIQ/
│
├── static/                    # CSS, images (if any)
├── templates/
│   └── index.html             # Main HTML form
├── model/                     
│   └── model.pkl              # Trained Linear Regression model
├── app.py                     # Flask backend application
├── data/                      # Cleaned dataset (CSV)
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/BLRHomeIQ.git
cd BLRHomeIQ
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

Then, open your browser and go to:
`http://localhost:5000`

---

## 🌐 Deployment

You can deploy this app using:

* [Render](https://render.com)
* [Railway](https://railway.app)
* [Heroku](https://heroku.com)

---

## 📌 Future Enhancements

* ✅ Add input validation
* 📊 Integrate price trend charts
* 📍 Add map support for locations
* 🤖 Try advanced ML models like XGBoost or Random Forest

---
