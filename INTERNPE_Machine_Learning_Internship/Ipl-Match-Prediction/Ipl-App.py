import pandas as pd
import streamlit as st
from PIL import Image
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


st.set_page_config(page_title="IPL Winner Predictor", layout="centered")


TEAM_MAP = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
}

ACTIVE_TEAMS = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad",
]

VENUE_MAP = {
    "ACA-VDCA Cricket Stadium": "ACA-VDCA Cricket Stadium",
    "Arun Jaitley Stadium": "Arun Jaitley Stadium",
    "Arun Jaitley Stadium, Delhi": "Arun Jaitley Stadium",
    "Barsapara Cricket Stadium, Guwahati": "Barsapara Cricket Stadium",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium": "Ekana Cricket Stadium",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow": "Ekana Cricket Stadium",
    "Brabourne Stadium": "Brabourne Stadium",
    "Brabourne Stadium, Mumbai": "Brabourne Stadium",
    "Dr DY Patil Sports Academy": "Dr DY Patil Sports Academy",
    "Dr DY Patil Sports Academy, Mumbai": "Dr DY Patil Sports Academy",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium": "ACA-VDCA Cricket Stadium",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam": "ACA-VDCA Cricket Stadium",
    "Eden Gardens": "Eden Gardens",
    "Eden Gardens, Kolkata": "Eden Gardens",
    "Ekana Cricket Stadium": "Ekana Cricket Stadium",
    "Feroz Shah Kotla": "Arun Jaitley Stadium",
    "Himachal Pradesh Cricket Association Stadium": "HPCA Stadium, Dharamsala",
    "Himachal Pradesh Cricket Association Stadium, Dharamsala": "HPCA Stadium, Dharamsala",
    "M Chinnaswamy Stadium": "M Chinnaswamy Stadium",
    "M Chinnaswamy Stadium, Bengaluru": "M Chinnaswamy Stadium",
    "M.Chinnaswamy Stadium": "M Chinnaswamy Stadium",
    "MA Chidambaram Stadium": "MA Chidambaram Stadium, Chepauk",
    "MA Chidambaram Stadium, Chepauk": "MA Chidambaram Stadium, Chepauk",
    "MA Chidambaram Stadium, Chepauk, Chennai": "MA Chidambaram Stadium, Chepauk",
    "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur": "Mullanpur Stadium",
    "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh": "Mullanpur Stadium",
    "Maharashtra Cricket Association Stadium": "Maharashtra Cricket Association Stadium",
    "Maharashtra Cricket Association Stadium, Pune": "Maharashtra Cricket Association Stadium",
    "Narendra Modi Stadium": "Narendra Modi Stadium",
    "Narendra Modi Stadium, Ahmedabad": "Narendra Modi Stadium",
    "Punjab Cricket Association IS Bindra Stadium": "PCA Stadium, Mohali",
    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh": "PCA Stadium, Mohali",
    "Punjab Cricket Association IS Bindra Stadium, Mohali": "PCA Stadium, Mohali",
    "Punjab Cricket Association Stadium, Mohali": "PCA Stadium, Mohali",
    "Rajiv Gandhi International Stadium": "Rajiv Gandhi International Stadium, Uppal",
    "Rajiv Gandhi International Stadium, Uppal": "Rajiv Gandhi International Stadium, Uppal",
    "Rajiv Gandhi International Stadium, Uppal, Hyderabad": "Rajiv Gandhi International Stadium, Uppal",
    "Sardar Patel Stadium, Motera": "Narendra Modi Stadium",
    "Sawai Mansingh Stadium": "Sawai Mansingh Stadium",
    "Sawai Mansingh Stadium, Jaipur": "Sawai Mansingh Stadium",
    "Wankhede Stadium": "Wankhede Stadium",
    "Wankhede Stadium, Mumbai": "Wankhede Stadium",
}

TEAM_LOGOS = {
    "Mumbai Indians": "Logos/mi.png",
    "Chennai Super Kings": "Logos/csk.webp",
    "Royal Challengers Bengaluru": "Logos/rcb.png",
    "Kolkata Knight Riders": "Logos/kkr.png",
    "Sunrisers Hyderabad": "Logos/srh.png",
    "Delhi Capitals": "Logos/dc.jpg",
    "Punjab Kings": "Logos/pk.png",
    "Rajasthan Royals": "Logos/rr.png",
    'Gujrat titans':'Logos/gt.png',
    'Lucknow Super Gient':'Logos/lsg.png'
}

TEAM_HOME_VENUES = {
    "Chennai Super Kings": ["MA Chidambaram Stadium, Chepauk"],
    "Mumbai Indians": ["Wankhede Stadium"],
    "Kolkata Knight Riders": ["Eden Gardens"],
    "Royal Challengers Bengaluru": ["M Chinnaswamy Stadium"],
    "Delhi Capitals": ["Arun Jaitley Stadium", "ACA-VDCA Cricket Stadium"],
    "Punjab Kings": [
        "PCA Stadium, Mohali",
        "HPCA Stadium, Dharamsala",
    ],
    "Rajasthan Royals": ["Sawai Mansingh Stadium"],
    "Sunrisers Hyderabad": ["Rajiv Gandhi International Stadium, Uppal"],
    "Gujarat Titans": ["Narendra Modi Stadium"],
    "Lucknow Super Giants": ["Ekana Cricket Stadium"],
}


def load_logo(path):
    img = Image.open(path)
    return img.resize((150, 150))


def normalize_venue(venue):
    if pd.isna(venue):
        return venue
    return VENUE_MAP.get(venue, venue)


@st.cache_data
def load_match_data():
    df = pd.read_csv("ipl.csv")

    for col in ["team1", "team2", "winner", "toss_winner"]:
        df[col] = df[col].replace(TEAM_MAP)

    df["venue"] = df["venue"].apply(normalize_venue)

    df = df[
        df["winner"].notna()
        & df["target_runs"].notna()
        & df["result"].isin(["runs", "wickets"])
        & (df["super_over"] == "N")
        & df["team1"].isin(ACTIVE_TEAMS)
        & df["team2"].isin(ACTIVE_TEAMS)
        & df["winner"].isin(ACTIVE_TEAMS)
        & df["toss_winner"].isin(ACTIVE_TEAMS)
    ].copy()

    df["runs_scored"] = (df["target_runs"] - 1).astype(int)

    return df[["team1", "team2", "venue", "toss_winner", "runs_scored", "winner"]].copy()


@st.cache_resource
def train_model():
    df = load_match_data()

    X = df[["team1", "team2", "venue", "toss_winner", "runs_scored"]]
    y = df["winner"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["team1", "team2", "venue", "toss_winner"]),
            ("num", "passthrough", ["runs_scored"]),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=250, max_depth=10, min_samples_leaf=4, random_state=42)),
        ]
    )

    model.fit(X, y)
    return model, df


def find_home_team(team1, team2, venue):
    for team, venues in TEAM_HOME_VENUES.items():
        if venue in venues and team in [team1, team2]:
            return team
    return None


model, history_df = train_model()
teams = sorted(set(history_df["team1"]).union(set(history_df["team2"])))
venues = sorted(history_df["venue"].dropna().unique().tolist())

st.title("IPL Match Winner Predictor")
st.write("Predict whether team1 will defend the score or team2 will chase it successfully.")

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", teams)

with col2:
    team2 = st.selectbox("Team 2", teams, index=1 if len(teams) > 1 else 0)

toss_winner = st.selectbox("Toss Winner", [team1, team2] if team1 != team2 else [team1])
venue = st.selectbox("Venue", venues)
runs_scored = st.number_input("First Innings Runs Scored", min_value=50, max_value=300, value=180, step=1)

logo_col1, logo_col2 = st.columns(2)

with logo_col1:
    if team1 in TEAM_LOGOS:
        st.image(load_logo(TEAM_LOGOS[team1]))
    st.caption(f"Team 1: {team1}")

with logo_col2:
    if team2 in TEAM_LOGOS:
        st.image(load_logo(TEAM_LOGOS[team2]))
    st.caption(f"Team 2: {team2}")

home_team = find_home_team(team1, team2, venue)
if home_team:
    st.info(f"Home venue advantage check: {home_team} is the home team for this venue.")
else:
    st.caption("This venue is treated as neutral for the selected teams.")

if team1 == team2:
    st.warning("Please choose two different teams.")

if st.button("Predict Winner", type="primary") and team1 != team2:
    input_data = pd.DataFrame(
        {
            "team1": [team1],
            "team2": [team2],
            "venue": [venue],
            "toss_winner": [toss_winner],
            "runs_scored": [int(runs_scored)],
        }
    )

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    classes = model.classes_
    probability_map = dict(zip(classes, probabilities))
    winning_probability = probability_map.get(prediction, 0) * 100

    st.subheader("Prediction Result")
    st.success(f"Predicted Winner: {prediction}")
    st.write(f"Winning Probability: {winning_probability:.2f}%")

    if prediction == team2:
        st.write(f"Interpretation: {team2} is predicted to chase {int(runs_scored)} successfully.")
    else:
        st.write(f"Interpretation: {team1} is predicted to defend {int(runs_scored)}.")
