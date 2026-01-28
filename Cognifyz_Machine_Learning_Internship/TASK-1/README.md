# Task 1: Restaurant Rating Prediction

## 📌 Objective
The objective of this task is to build a **machine learning regression model** to predict the **aggregate rating of a restaurant** based on features such as pricing, customer engagement, service availability, and location-related attributes.

This task is completed as part of the **Machine Learning Internship at Cognifyz Technologies**.

---

## 📂 Dataset
The dataset contains structured information about restaurants, including numerical and categorical features related to ratings, votes, pricing, and services.  
The target variable for prediction is **Aggregate Rating**.

---

## 🔍 Approach

### 1. Data Preprocessing
- Handled missing values:
  - Median for numerical features
  - Mode for categorical features
- Encoded categorical variables using label encoding
- Removed non-informative columns (e.g., restaurant name, address, IDs)

### 2. Feature & Target Selection
- **Features (X):** Relevant restaurant attributes
- **Target (y):** Aggregate restaurant rating

### 3. Model Training
Two regression models were implemented:
- **Linear Regression** (baseline model)
- **Decision Tree Regressor** (to capture non-linear patterns)

The dataset was split into training and testing sets using an **80–20 split**.

---

## 📊 Model Evaluation
The models were evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Performance Summary
- Linear Regression provided a baseline performance.
- Decision Tree Regressor outperformed the baseline by capturing non-linear relationships in the data.

---

## 📈 Model Interpretation & Visualization
- Feature coefficients and feature importance were analyzed to understand influential factors.
- Visualizations such as **Actual vs Predicted Ratings** and **Feature Importance plots** were used for interpretation.

Key observations indicate that **pricing, customer engagement, and service availability** significantly influence restaurant ratings.

---

## ✅ Conclusion
The **Decision Tree Regressor** was selected as the final model due to its superior predictive performance and interpretability. The task demonstrates how machine learning regression techniques can be effectively applied to real-world restaurant data.

---

## 🛠️ Tools & Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook  

