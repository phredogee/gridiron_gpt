# gpt/pipelines/semantic_pipeline.py

class SemanticPipeline:
    def __init__(self, df, le_position, le_weather, model):
        self.df = df
        self.le_position = le_position
        self.le_weather = le_weather
        self.model = model

    def predict(self, position, weather):
        pos_enc = self.le_position.transform([position])[0]
        weather_enc = self.le_weather.transform([weather])[0]
        return self.model.predict([[pos_enc, weather_enc]])[0]
