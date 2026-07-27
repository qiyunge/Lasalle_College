from .image import Image

class RealImage(Image):

    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print("Displaying real image.")