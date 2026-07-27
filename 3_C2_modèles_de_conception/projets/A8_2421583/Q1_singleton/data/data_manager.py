from core import Singleton


class DataManager(Singleton):
    def load_data(self):
        # Code to load data from a source (e.g., file, database)
         print("Loading  data...")
         return ["data1", "data2", "data3"]