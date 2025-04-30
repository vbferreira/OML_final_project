from fastapi import FastAPI
from app.schemas import InputData
from app.model_loader import load_model
import pandas as pd

app = FastAPI(
    title="Rumos Bank Credit Default Predictor",
    description="API para prever incumprimento de crédito",
    version="1.0.0"
)

model = load_model()

@app.get("/")
def root():
    return {"message": "API Rumos Bank ativa. Use /predict para enviar dados."}

@app.post("/predict")
def predict(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    prob = model.predict_proba(input_df)[0][1]
    pred = int(prob >= 0.5)

    return {
        "prediction": pred,
        "probability": round(prob, 4)
    }
