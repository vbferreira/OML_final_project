import mlflow
import mlflow.sklearn

def load_model():
    model_uri = "mlruns/773736397415668486/2ad5aca2276f49cca441ed60c30d0679/artifacts/model"
    model = mlflow.sklearn.load_model(model_uri)
    return model


