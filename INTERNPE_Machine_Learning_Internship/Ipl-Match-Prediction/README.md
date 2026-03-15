# 🏏 IPL Match Winner Predictor

A **Machine Learning powered Streamlit web application** that predicts the winner of an IPL match based on match conditions such as teams, venue, toss winner, and first innings score.

The model is trained on **historical IPL match data** and uses a **Random Forest Classifier** to estimate the probability of each team winning.

---

# 📌 Project Overview

This project demonstrates a complete **end-to-end ML workflow**:

1. Data preprocessing and cleaning
2. Feature selection
3. Model training using Random Forest
4. Model deployment using Streamlit
5. Interactive user interface for predictions

Users can input match conditions and receive a **predicted winner along with the winning probability**.

---

# ⚙️ Features

✔ Predict IPL match winners
✔ Interactive Streamlit web interface
✔ Team logos displayed for better UI
✔ Home venue advantage detection
✔ Winning probability estimation
✔ Automated data preprocessing pipeline

---

# 📊 Input Features

The prediction model uses the following features:

| Feature         | Description                       |
| --------------- | --------------------------------- |
| **Team 1**      | Team batting first                |
| **Team 2**      | Team chasing                      |
| **Venue**       | Stadium where the match is played |
| **Toss Winner** | Team that won the toss            |
| **Runs Scored** | First innings score               |

The model predicts whether:

* **Team 1 will defend the score**, or
* **Team 2 will chase the target successfully**

---

# 🧠 Machine Learning Model

The prediction model is built using:

* **Algorithm:** Random Forest Classifier
* **Framework:** Scikit-Learn
* **Encoding:** One-Hot Encoding for categorical variables
* **Pipeline:** Preprocessing + Model training combined

From the application code:

* Categorical Features: `team1`, `team2`, `venue`, `toss_winner`
* Numerical Feature: `runs_scored`
* Trees used: **250**
* Maximum depth: **10**

The preprocessing and training pipeline is defined in the application. 

---

# 🗂 Dataset

The model is trained on a historical IPL dataset containing match details such as:

* Teams
* Venue
* Toss winner
* Target score
* Match result

Dataset file used:

```
ipl.csv
```

The dataset is filtered to include only **active IPL teams** to ensure realistic predictions.

---

# 🖥 Application Interface

The Streamlit app allows users to:

1️⃣ Select **Team 1**
   2️⃣ Select **Team 2**

3️⃣ Select **Toss Winner**

4️⃣ Select **Venue**

5️⃣ Enter **First Innings Score**

After clicking **Predict Winner**, the app displays:

* 🏆 Predicted winner
* 📊 Winning probability
* 📖 Interpretation of the result

---

# 📁 Project Structure

```
IPL-Winner-Predictor
│
├── ipl.csv
├── ipl_winner_prediction_model.pkl
├── Ipl-App.py
├── Logos/
│
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/IPL-Winner-Predictor.git
cd IPL-Winner-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Example dependencies:

```
streamlit
pandas
scikit-learn
pillow
```

---

# ▶️ Running the Application

Run the Streamlit app:

```bash
streamlit run Ipl-App.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# 📷 Example Prediction

Example input:

```
Team 1: Royal Challengers Bengaluru
Team 2: Kolkata Knight Riders
Venue: Wankhede Stadium
Toss Winner: RCB
Runs Scored: 180
```

Output:

```
Predicted Winner: Kolkata Knight Riders
Winning Probability: 63%
```

Interpretation:

> KKR is predicted to successfully chase the target.

---

# ⚠️ Limitations

* Model is trained on **historical IPL data only**
* Does not consider:

  * Player form
  * Injuries
  * Team lineup
  * Weather conditions
  * Match pressure
* Predictions should be interpreted as **statistical estimates, not guarantees**

---

# 🔮 Future Improvements

Possible enhancements:

* Add **player statistics**
* Use **recent season data**
* Implement **XGBoost / LightGBM**
* Add **head-to-head statistics**
* Deploy online using **Streamlit Cloud**

---

# 👨‍💻 Author

**Mrinmoy Debnath**  |  AI-ML Enthusiast

