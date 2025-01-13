class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.radius = new_radius
        return new_radius

cake = Circle(12)
print(cake.get_radius())
print(cake.set_radius(15))
