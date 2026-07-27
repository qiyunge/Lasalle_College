from core import Singleton


class ModelTrainer(Singleton):
    def train_model(self, features):
        # Code to train a model using the extracted features
        print("Training model...")
        return {"model": "trained_model", 
                "features": features}