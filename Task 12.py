class Student:
    def __init__(self, name, surname, year, grades=dict()) -> None:
        self.name = name
        self.surname = surname
        self.year = year
        self.grades = grades
    def average_grade(self):
        return sum(self.grades.values())/len(self.grades.values())
man = Student("Яна", "Болдарева", 2, {"Математика":4, "Бизнес аналитика":5, "История":5})
print("Средний былл студента", man.average_grade())