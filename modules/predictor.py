def predict_action(model, le_position, le_weather, le_team, le_opp_team,
                   position, defense_rank, weather, week, team, opponent_team):
    # Encode categorical features
    pos_encoded = le_position.transform([position])[0]
    weather_encoded = le_weather.transform([weather])[0]
    team_encoded = le_team.transform([team])[0]
    opp_encoded = le_opp_team.transform([opponent_team])[0]

    features = [[pos_encoded, defense_rank, weather_encoded, week, team_encoded, opp_encoded]]
    prediction = model.predict(features)[0]
    return prediction
