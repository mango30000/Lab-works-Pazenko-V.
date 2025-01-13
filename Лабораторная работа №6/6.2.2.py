class Vehicle:

    def __init__(self,make,model,bak_topl):
        self.make = make
        self.model = model
        self.bak_topl = bak_topl

    def get_info(self):
        print("Марка автомобиля: {}".format(self.make))
        print('Модель автомобиля: {}'.format(self.model))
        print('Объем бака топлива: {} литров'.format(self.bak_topl))

class Car(Vehicle):
    def __init__(self,make, model, bak_topl, fuel_type):
        super().__init__(make,model,bak_topl)
        self.fuel_type = fuel_type
    def get_info(self):
        super().get_info()
        print('Тип топлива: {}'.format(self.fuel_type))
    def rash_topl(self,km):
        self.bak_topl -= km * 12.3




# car = Vehicle('Genesis', 'G80', '200')
# car.get_info() #Марка автомобиля: Genesis  Модель автомобиля: G80

avto1 = Car('Genesis', 'G80',200,'fjfj')
print(avto1.bak_topl)
# avto1.get_info() #Марка автомобиля: Genesis  Модель автомобиля: G80  Тип топлива: АИ-95
avto1.rash_topl(100)
print(avto1.bak_topl)

