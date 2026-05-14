# modules/predictor.py

def predict_action(
    model, le_position, le_weather,
    le_team, le_opp_team,
    position, defense_rank, weather, week, team, opponent_team
):
    print("🧠 Predicting action...")

    encoded_position = le_position.transform([position])[0]
    encoded_weather = le_weather.transform([weather])[0]

    features = [[encoded_position, encoded_weather, defense_rank, week]]
    prediction = model.predict(features)[0]

    return prediction
