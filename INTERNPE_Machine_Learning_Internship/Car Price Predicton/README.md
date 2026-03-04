# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project builds a **Machine Learning regression model** that predicts the **selling price of a car** based on its features.

The model analyzes attributes such as **company, manufacturing year, fuel type, and kilometers driven** to estimate the car's market value.

This project demonstrates key machine learning concepts such as **data preprocessing, feature encoding, model training, and prediction**.

---

## 📊 Dataset Information

The dataset contains information about used cars and their selling prices.

### 🔢 Features

| Feature | Description |
|-------|-------------|
| Company | Brand of the car |
| Year | Manufacturing year |
| Kms Driven | Total kilometers driven |
| Fuel Type | Petrol / Diesel / CNG |

### 🎯 Target Variable

| Feature | Description |
|--------|-------------|
| Price | Selling price of the car |

---

## 🤖 Machine Learning Models Used

Two regression models were trained and compared:

- **Linear Regression**
- **Random Forest Regressor**

The models were evaluated using the **R² Score** to determine prediction performance.

---

## ⚙️ Project Workflow


    Data Loading
    ↓
    Data Cleaning
    ↓
    Handling Missing Values
    ↓
    Feature Encoding
    ↓
    Train-Test Split
    ↓
    Model Training
    ↓
    Model Evaluation
    ↓
    Price Prediction


---

## 🛠️ Libraries Used

| Library | Purpose |
|------|------|
| 🐍 Python | Programming Language |
| 📊 Pandas | Data Manipulation |
| 🔢 NumPy | Numerical Computation |
| 🤖 Scikit-Learn | Machine Learning Models |
| 📓 Jupyter Notebook | Development Environment |

---

## 🔍 Model Output

The trained model predicts the **estimated selling price of a car** based on input features such as company, year, fuel type, and kilometers driven.

Example prediction:


    Input:
    Company: Tata
    Year: 2018
    Kms Driven: 27000
    Fuel Type: Diesel

    Predicted Price ≈ ₹3,49,000

---

## 📁 Files Included

    Car_Price_Prediction
    │
    ├── Car_Price_Predictor.ipynb
    ├── quikr_car.csv
    └── README.md


---

## 👨‍💻 Author

**Mrinmoy Debnath**  
Machine Learning Enthusiast  

🔗 GitHub: https://github.com/Mrinmoy5-rgb