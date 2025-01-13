class Vehicle:
    make = 'Genesis'
    model = 'G80'

    def get_info(self):
        print("Марка автомобиля: {}".format(self.make))
        print('Модель автомобиля: {}'.format(self.model))

class Car(Vehicle):
    fuel_type = 'АИ-95'
    def __init__(self):
        super().__init__()
    def get_info(self):
        print("Марка автомобиля: {}".format(self.make))
        print('Модель автомобиля: {}'.format(self.model))
        print('Тип топлива: {}'.format(self.fuel_type))

avto1 = Car()
avto1.get_info()


car = Vehicle('black')
print(car.__class__.make)
print(car.__class__.model)
car.get_info()