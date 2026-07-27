from core import Singleton


class FeatureExtractor(Singleton):
    def extract_features(self, data):
        # Code to extract features from the data
        print("Extracting features...")
        return ["feature1", "feature2", "feature3"]