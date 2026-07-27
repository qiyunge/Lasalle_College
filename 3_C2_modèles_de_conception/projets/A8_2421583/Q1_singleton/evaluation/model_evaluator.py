from core import Singleton

class ModelEvaluator(Singleton):
    def evaluate_model(self, model, test_data):
        # Code to evaluate the trained model using test data
        print("Evaluating model...")
        return {"accuracy": 0.95, "loss": 0.05}