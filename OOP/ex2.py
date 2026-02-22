class Rectangle:
    def __init__(self, width:float = 1.0, height:float = 1.0, color:str = "white"):
        self.width = width
        self.height = height
        self.color = color

    def area(self)->float:
        return self.width * self.height

    def perimeter(self)->float:
        return 2 * (self.width + self.height)
    


if __name__ == "__main__":
    rect1 = Rectangle()
    print(f"Area: {rect1.area()}, Perimeter: {rect1.perimeter()}, Color: {rect1.color}")

    rect2 = Rectangle(2.0, 3.0, "red")
    print(f"Area: {rect2.area()}, Perimeter: {rect2.perimeter()}, Color: {rect2.color}")