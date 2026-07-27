from images import Image

class ImageView:
    def __init__(self):
        self.images = []
    
    def add_image(self, image:Image):
        self.images.append(image)

    def display_images(self, index:int):
        if index < 0 or index >= len(self.images):
            print("Invalid index.")
            return
        self.images[index].display()