import os
import pickle

import pandas as pd
import streamlit as st


st.set_page_config(page_title="🏏IPL Winner Predictor", layout="centered")

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "IPL_Winner_Prediction_Clean.pkl")

VENUE_ALIASES = {
    "Eden Gardens, Kolkata": "Eden Gardens",
}


def normalize_venue(venue):
    venue = VENUE_ALIASES.get(venue, venue)
    venue_lower = venue.strip().lower()
    if "eden" in venue_lower and "garden" in venue_lower:
        return "Eden Gardens"
    return venue


@st.cache_resource
def load_model_bundle(_model_mtime):
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def confidence_label(probability):
    if probability >= 75:
        return "High"
    if probability >= 60:
        return "Moderate"
    return "Low"


bundle = load_model_bundle(os.path.getmtime(MODEL_PATH))
model = bundle["model"]
teams = bundle["teams"]
venues = sorted({normalize_venue(venue) for venue in bundle["venues"]})
toss_options = bundle["toss_options"]

st.title("IPL Winner Predictor")
st.write("Predict the match winner using current IPL teams and match conditions.")

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", teams)

with col2:
    default_team2_index = 1 if len(teams) > 1 else 0
    team2 = st.selectbox("Team 2", teams, index=default_team2_index)

venue = st.selectbox("Venue", venues)
toss_winner = st.selectbox(
    "Toss Winner",
    [team1, team2] if team1 != team2 else [team1],
)
toss_decision = st.selectbox("Toss Decision", toss_options)
first_innings_score = st.number_input(
    "First Innings Score", min_value=50, max_value=300, value=180, step=1
)

if team1 == team2:
    st.warning("Please choose two different teams.")

if st.button("Predict Winner", type="primary") and team1 != team2:
    input_df = pd.DataFrame(
        {
            "team1": [team1],
            "team2": [team2],
            "venue": [normalize_venue(venue)],
            "toss_winner": [toss_winner],
            "toss_decision": [toss_decision],
            "first_innings_score": [int(first_innings_score)],
        }
    )

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    probability_map = dict(zip(model.classes_, probabilities))

    team1_probability = probability_map.get(team1, 0.0)
    team2_probability = probability_map.get(team2, 0.0)
    total_probability = team1_probability + team2_probability

    if total_probability > 0:
        team1_probability = (team1_probability / total_probability) * 100
        team2_probability = (team2_probability / total_probability) * 100
    else:
        team1_probability = 50.0
        team2_probability = 50.0

    winning_probability = (
        team1_probability if prediction == team1 else team2_probability
    )

    st.subheader("Prediction Result")
    st.success(f"Predicted Winner: {prediction}")
    st.write(
        f"Win Probability: {winning_probability:.2f}% ({confidence_label(winning_probability)} confidence)"
    )

    st.subheader("Match Intuition")
    if prediction == team1:
        st.info(
            f"{team1} looks more likely to defend {int(first_innings_score)} at {venue}. "
            f"The toss went to {toss_winner}, who chose to {toss_decision}."
        )
    else:
        st.info(
            f"{team2} looks more likely to chase or control the match at {venue}. "
            f"The toss went to {toss_winner}, who chose to {toss_decision}."
        )

    st.write(f"{team1}: {team1_probability:.2f}%")
    st.write(f"{team2}: {team2_probability:.2f}%")
