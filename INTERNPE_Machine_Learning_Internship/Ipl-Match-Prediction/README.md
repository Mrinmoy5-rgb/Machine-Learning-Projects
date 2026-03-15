# 🏏 IPL Match Winner Prediction

This project predicts the winner of an Indian Premier League (IPL) match using match conditions, teams, and toss information.

It includes:
- A **trained classification model** (pickle file) for winner prediction.
- A **Streamlit web app** (`Ipl-App.py`) to interactively predict match outcomes.
- A **Jupyter notebook** (`IPL_Winner_Prediction_Clean.ipynb`) used to explore the dataset, train models, and evaluate performance.

---

## 📁 Repository Structure

- `Ipl-App.py` – Streamlit application for end-user predictions.
- `IPL_Winner_Prediction_Clean.ipynb` – Notebook for data cleaning, feature engineering, training, and evaluation.
- `IPL_Winner_Prediction_Clean.pkl` – Serialized trained model bundle (model + metadata).
- `ipl.csv` – Dataset used for training and analysis.
- `requirements.txt` – Python dependencies.

---

## 🚀 Getting Started (Run the App)

### 1) Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the Streamlit app

```bash
streamlit run Ipl-App.py
```

Then open the displayed URL (usually `http://localhost:8501`) to use the predictor.

---

## 🧠 How It Works

The app collects the following inputs:
- **Team 1 / Team 2** (playing teams)
- **Venue**
- **Toss winner** and **toss decision** (bat/field)
- **First innings score**

It then uses the trained model to predict the likely match winner and provides a probability-based confidence level.

---

## 📊 Training / Model Development

To retrain or explore the model:
1. Open `IPL_Winner_Prediction_Clean.ipynb`.
2. Follow the steps to:
   - Load and clean `ipl.csv`
   - Perform feature engineering and encoding
   - Train and evaluate classification models (e.g., Random Forest, Logistic Regression)
   - Serialize the final model bundle to `IPL_Winner_Prediction_Clean.pkl`

---

## 🗂 Dataset

The dataset (`ipl.csv`) contains historical IPL match data including:
- Teams involved
- Venue
- Toss winner and decision
- Score details
- Match winner

> Note: The performance of the model depends heavily on the dataset's quality and the range of seasons covered.

---

## 📝 Notes & Limitations

- Predictions are based on historical data and do not account for real-time factors like player injuries, weather changes, or last-minute team changes.
- The model assumes both teams and venues are present in the training data.

---

## 👤 Author

**Mrinmoy Debnath**  
Machine Learning Enthusiast  

🔗 GitHub: https://github.com/Mrinmoy5-rgb
