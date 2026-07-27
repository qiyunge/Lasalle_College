from application import ImageView
from images import ProxyImage


def main():
    image_view = ImageView()

    # Add images to the view
    image_view.add_image(ProxyImage("image1.jpg"))
    image_view.add_image(ProxyImage("image2.jpg"))
    image_view.add_image(ProxyImage("image3.jpg"))

    # Display images
    print("Displaying images:")
    image_view.display_images(0)
    image_view.display_images(1)
    image_view.display_images(2)

if __name__ == "__main__":
    main()