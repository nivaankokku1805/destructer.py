class Circle:
    def __init__(self, radius):
        """
        Constructor to initialize the radius of the circle.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def compute_area(self):
        """
        Method to compute the area of the circle.
        Formula: Area = π * radius^2
        """
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        """
        Method to compute the perimeter (circumference) of the circle.
        Formula: Perimeter = 2 * π * radius
        """
        return 2 * math.pi * self.radius


# Example usage
if __name__ == "__main__":
    try:
        # Input radius from the user
        radius = float(input("Enter the radius of the circle: "))
        
        # Create a Circle object
        circle = Circle(radius)
        
        # Compute and display the area and perimeter
        print(f"Area of the circle: {circle.compute_area():.2f}")
        print(f"Perimeter of the circle: {circle.compute_perimeter():.2f}")
    except ValueError as e:
        print(f"Error: {e}")