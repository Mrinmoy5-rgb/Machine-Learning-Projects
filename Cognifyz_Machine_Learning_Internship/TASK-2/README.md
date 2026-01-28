# Task 2: Restaurant Recommendation System 🍽️

## 📌 Objective
The objective of this task is to develop a **content-based restaurant recommendation system** that suggests restaurants to users based on their preferences such as **cuisine type, city, and price range**.

This task was completed as part of the **Machine Learning Internship at Cognifyz Technologies**.

---

## 📂 Dataset
The dataset provided for this task contains information about restaurants, including:

- Restaurant name
- Cuisines
- City
- Price range
- Aggregate rating
- Other service and location-related attributes

Only relevant features were selected for building the recommendation system.

---

## 🔍 Methodology

### 1. Data Preprocessing
- Handled missing values in the **Cuisines** column
- Selected relevant columns for recommendation
- Converted categorical variables into numerical form using **One-Hot Encoding**

---

### 2. User Preference Definition
User preferences were defined manually to simulate a real-world recommendation request.

Example preferences:
- **Cuisine:** North Indian
- **City:** New Delhi
- **Price Range:** 3

---

### 3. Content-Based Filtering
- Each restaurant was represented as a numerical feature vector
- User preferences were transformed into a matching feature vector
- **Cosine similarity** was used to measure similarity between user preferences and restaurant attributes

---

### 4. Recommendation Generation
- Restaurants were ranked based on similarity scores
- Aggregate ratings were used to prioritize higher-quality restaurants
- The **top 10 most relevant restaurants** were selected as final recommendations

---

## 📊 Final Output
The final output of the system is a table displaying the **top 10 recommended restaurants**, including:

- Restaurant Name
- Cuisines
- City
- Price Range
- Aggregate Rating

The recommendations are personalized based on the user’s preferences.

---

## 🛠️ Tools & Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## ✅ Conclusion
A content-based restaurant recommendation system was successfully developed using similarity-based filtering. Since no explicit user feedback or labels were available, supervised learning was not applicable. The approach provides interpretable and relevant recommendations based on user-defined preferences.

---

## 👤 Author
**Mrinmoy Debnath**

