class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self,new_password):
        self.__password = new_password
    def check_password(self,password):
        if self.__password == password:
            return True
        else:
            return False

person = UserAccount('flowafrain', 'flofir@mail.ru', 'dfh2345')
print(person.check_password('dfh2345')) #True
person.set_password('ofkfff')
print(person.check_password('ofkfff')) #True
print(person.check_password('11111')) #False

