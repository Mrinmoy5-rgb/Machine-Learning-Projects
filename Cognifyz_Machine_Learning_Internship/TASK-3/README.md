# Task 3: Cuisine Classification 🍽️

## 📌 Objective
The objective of this task is to develop a **machine learning classification model** to **classify restaurants based on their cuisines** using structured restaurant attributes.

This task was completed as part of the **Machine Learning Internship at Cognifyz Technologies**.

---

## 📂 Dataset
The dataset contains structured information about restaurants, including:

- City and location details
- Pricing and service-related attributes
- Customer engagement metrics (votes, ratings)
- Cuisine information

For this task, the **primary cuisine** of each restaurant was considered as the target class.

---

## 🔍 Methodology

### 1. Data Preprocessing
- Handled missing values in both numerical and categorical features
- Extracted the **primary cuisine** from multiple cuisine entries
- Selected relevant features for classification
- Encoded categorical variables and scaled numerical features using a preprocessing pipeline

---

### 2. Train–Test Split
- The dataset was divided into **training and testing sets** to evaluate model performance on unseen data
- Stratified sampling was used to preserve cuisine distribution

---

### 3. Model Selection & Training
- A **Random Forest Classifier** was selected due to its ability to:
  - Handle non-linear relationships
  - Work effectively with mixed feature types
  - Perform well in multi-class classification problems

The model was trained using the training dataset within a pipeline to avoid data leakage.

---

## 📊 Model Evaluation
The model was evaluated on the test dataset using the following classification metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Confusion Matrix**

These metrics provided both overall and class-wise insights into model performance.

---

## 📈 Cuisine-Wise Performance Analysis
- The model performed better for **frequently occurring cuisines** such as *North Indian, Cafe, and Bakery* due to sufficient training samples.
- **Rare cuisines** showed lower recall and precision because of limited data availability.
- The results highlight the impact of **class imbalance** in multi-class classification problems.

---

## ⚠️ Challenges & Biases Identified
- Significant **class imbalance** across cuisine categories
- Several cuisines had very few samples, leading to poor generalization
- Restaurants often serve multiple cuisines, but the model predicts only a single primary cuisine
- Structured numerical features may not fully capture culinary characteristics

---

## 🛠️ Tools & Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## ✅ Conclusion
A machine learning model was successfully developed to classify restaurants based on their cuisines. While the model achieved reasonable performance for common cuisines, its effectiveness was limited for rare cuisines due to data imbalance and sparsity. Future improvements could include data balancing techniques, multi-label classification, and the use of textual features.

---

## 👤 Author
**Mrinmoy Debnath**

