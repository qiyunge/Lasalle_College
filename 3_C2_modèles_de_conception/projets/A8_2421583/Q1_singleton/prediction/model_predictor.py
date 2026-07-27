from core import Singleton

class ModelPredictor(Singleton):
    def predict(self, model, new_data):
        # Code to make predictions using the trained model and new data
        print("Making predictions...")
        return ["prediction1", "prediction2", "prediction3"]