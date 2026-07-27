from data import DataManager
from features import FeatureExtractor
from training import ModelTrainer
from evaluation import ModelEvaluator
from prediction import ModelPredictor

def main():
    # Step 1: Load data
    data_manager = DataManager()
    data = data_manager.load_data()

    # Step 2: Extract features
    feature_extractor = FeatureExtractor()
    features = feature_extractor.extract_features(data)

    # Step 3: Train model
    model_trainer = ModelTrainer()
    trained_model = model_trainer.train_model(features)

    # Step 4: Evaluate model
    model_evaluator = ModelEvaluator()
    evaluation_results = model_evaluator.evaluate_model(trained_model, data)

    # Step 5: Make predictions
    model_predictor = ModelPredictor()
    predictions = model_predictor.predict(trained_model, data)

    # Print results
    print("Evaluation Results:", evaluation_results)
    print("Predictions:", predictions)      

if __name__ == "__main__":
    main()