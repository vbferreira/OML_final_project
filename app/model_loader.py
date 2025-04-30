


# Código antigo com MLflow
#import mlflow
i#mport mlflow.sklearn
# import mlflow
# import mlflow.sklearn
# def load_model():
#     model_uri = "mlruns/773736397415668486/2ad5aca2276f49cca441ed60c30d0679/artifacts/model"
#     model = mlflow.sklearn.load_model(model_uri)
#     return model


import os
import joblib


def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "model_rf_compressed.joblib")
    model = joblib.load(model_path)
    return model
