class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def get_info(self):
        print('Имя сотрудника: {}'.format(self.name))
        print('ID сотрудника: {}'.format(self.id))

# sotr = Employee('Bob','ab12')
# sotr.get_info() #Имя сотрудника: Bob  ID сотрудника: ab12

class Manager(Employee):
    def __init__(self,name, id, department):
        Employee.__init__(self, name,id)
        self.department = department
    def get_info(self):
         super().get_info()
         print('Отдел: {}'.format(self.department))
    def manage_project(self):
        print('{} управляет проектами'.format(self.name))

#sotr = Manager('Bob','ab12', 'design')
#sotr.get_info() #Имя сотрудника: Bob  ID сотрудника: ab12  Отдел: design
#sotr.manage_project() #Bob управляет проектами

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self,name, id)
        self.specialization = specialization
    def perform_maintenance(self):
        print('{} выполняет техническое обслуживание'.format(self.name))

# sotr = Technician('Bob', 'ab12', 'Technic')
# sotr.perform_maintenance() #Bob выполняет техническое обслуживание

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name,id, specialization)
        self.a = []

    def add_employee(self,s):
        self.a.append(s)
    def get_team_info(self):
        if self.a:
            print('Информация о сотрудниках:')
            for s in self.a:
                print(f"Имя сотрудника: {s.name}. ID: {s.id}. Отдел: {s.department}. Специализация: {s.specialization}")
# sdkflsf = TechManager('bob','340','design','robot')
# sdkflsf.perform_maintenance()
s1 = TechManager('Bob','340','design','robot')
s2 = TechManager('Kate','342','design','robot')
s3 = TechManager('Ali','340','design','background')

s1.add_employee(s1)
s1.add_employee(s2)
s1.add_employee(s3)

s1.get_team_info()
