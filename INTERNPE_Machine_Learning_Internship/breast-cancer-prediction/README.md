# 🧠 Breast Cancer Prediction using Machine Learning

## 🚀 Project Overview

This project focuses on building a **Machine Learning model** to predict whether a tumor is **Malignant (Cancerous)** or **Benign (Non-cancerous)** using medical diagnostic data.

The model is trained on the Breast Cancer dataset and follows a complete **end-to-end ML pipeline**, including preprocessing, model training, evaluation, and prediction.

---

## 🎯 Objective

To develop a reliable classification model that can assist in **early detection of breast cancer**, with a strong emphasis on minimizing **false negatives** (missing actual cancer cases).

---

## 📊 Dataset

* Source: Breast Cancer Wisconsin Dataset
* Total Samples: 569
* Features: 30 numerical features
* Target:

  * `M` → Malignant (1)
  * `B` → Benign (0)

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Matplotlib & Seaborn

---

## 🔄 Machine Learning Workflow

1. **Data Loading & Inspection**
2. **Data Cleaning**

   * Removed irrelevant columns (`id`, `Unnamed: 32`)
3. **Feature Engineering**

   * Encoded target variable
4. **Train-Test Split**
5. **Feature Scaling (StandardScaler)**
6. **Model Building**

   * K-Nearest Neighbors (KNN)
7. **Hyperparameter Tuning**

   * GridSearchCV with Cross-Validation
8. **Model Evaluation**

   * Accuracy
   * Confusion Matrix
   * Precision, Recall, F1-score

9. **Prediction on New Data**

---

## 🤖 Model Details

### K-Nearest Neighbors (KNN)

* Distance-based classification algorithm
* Sensitive to feature scaling
* Hyperparameter tuned:

  * `n_neighbors (K)` using GridSearchCV

---

## 📈 Evaluation Metrics

* **Accuracy**
* **Precision**
* **Recall (Most Important)** ⭐
* **F1-score**

> ⚠️ Special focus was given to **Recall**, as missing a cancer diagnosis (False Negative) is critical in healthcare applications.

---

## 🔮 Prediction

The model can take new patient data (30 features) and predict:

* ✅ Benign (No Cancer)
* ❌ Malignant (Cancer)

It also provides probability scores for better interpretation.

---

## 💡 Key Learnings

* Importance of **feature scaling** for distance-based models
* Role of **cross-validation** in reliable model selection
* Why **accuracy alone is not enough** in medical ML problems
* Understanding trade-offs between **precision and recall**

---

## 📁 Project Structure

```
├── data.csv
├── breast-cancer-model.ipynb
└── README.md
```

---

## 👤 Author

**Mrinmoy Debnath  ||  ML Enthusiast**

**💻 GitHub:** https://github.com/Mrinmoy5-rgb

