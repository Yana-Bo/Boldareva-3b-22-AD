class Employee:
    def __init__(self, name, age, pay) -> None:
        self.name = name
        self.age = age
        self.pay = pay
    def viev(self):
        print(f"Сотрудник {self.name}, возраст - {self.age} лет, заработная плата -  {self.pay} рублей")
m = Employee("Виктория", 28, 48500)
m.viev()