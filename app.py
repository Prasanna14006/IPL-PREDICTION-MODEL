from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import traceback
app = Flask(__name__)

import joblib
model = joblib.load("D:/github/NEW2-main/NEW2-main/xgboost_ipl_winner_model.pkl")


# Encoding dictionaries (example - update with your own values)
TEAM_ENCODING = {
    "CSK": 0,
    "MI": 1,
    "RCB": 2,
    "KKR": 3,
    "SRH": 4,
    "DC": 5,
    "RR": 6,
    "PBKS": 7,
    "LSG": 8,
    "GT": 9
}

VENUE_ENCODING = {
    "Chennai": 2,
    "Mumbai": 3,
    "Bangalore": 4,
    "Kolkata": 5,
    "Jaipur": 6,
    "Delhi": 7,
    "Mohali": 8,
    "Hyderabad": 9,
    "Ahmedabad": 10,
    "Lucknow": 11
}


TOSS_DECISION_ENCODING = {
    "Bat": 2,
    "Field": 3
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        # print("Received data:", data)

        # Validate inputs
        required_fields = ["team1", "team2", "venue", "toss_winner", "toss_decision"]
        # print(required_fields)
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # print(data["team1"])
        #print(TEAM_ENCODING)
        team1 = data["team1"].upper()
        team2 = data["team2"].upper()
        venue = data["venue"].capitalize()
        toss_winner = data["toss_winner"].upper()
        toss_decision = data["toss_decision"].capitalize()
        features = [
            TEAM_ENCODING[team1],
            TEAM_ENCODING[team2],
            TEAM_ENCODING[toss_winner],
            TOSS_DECISION_ENCODING[toss_decision]
        ]

        input=np.array(features).reshape(1,4)
        #print("Encoded features:", features)
        # print(input)
        
        # print(model.feature_names_in_)
        prediction = model.predict(input) # Convert to native int
        prediction = np.unique(prediction).tolist()
        pred = int(round(float(prediction[0])))

        reverse_team_encoding = {v: k for k, v in TEAM_ENCODING.items()}
        #print(reverse_team_encoding)
        return jsonify({
            "prediction": pred,
            "winner": reverse_team_encoding.get(pred, "Unknown")
        })

    except Exception as e:
        print("Prediction error:", str(e))
        traceback.print_exc()  # Add this for full error in console
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
