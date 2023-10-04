class Student:
    def __init__(self, surname="surname", name="name", patronymic="patronymic"):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def get_info(self):
        print(f"\t\tName: {self.surname} {self.name} {self.patronymic}")


class BudgetStudent(Student):
    def __init__(self, surname="surname", name="name", patronymic="patronymic", budget=0):
        super().__init__(surname, name, patronymic)
        self.stipend = budget

    def get_info(self):
        super().get_info()
        print(f"\t\tStipend: {self.stipend} uah")


class Group:
    def __init__(self, number=0, students=None):
        self.number = number
        self.students = students or []

    def get_info(self):
        print(f"Group: {self.number}")
        for i, student in enumerate(self.students):
            print(f"\tStudent #{i + 1}:")
            student.get_info()


class Discipline:
    def __init__(self, name="Discipline", credits_num=1, semester=1):
        self.name = name
        self.credits_num = credits_num
        self.semester = semester

    def get_info(self):
        print(f"\t\tDiscipline name: {self.name}")
        print(f"\t\tNumber of credits: {self.credits_num}")
        print(f"\t\tSemester of teaching: {self.semester}")


class Educator:
    def __init__(self, disciplines=None, surname="surname", name="name", patronymic="patronymic",
                 year_of_birth=0, teaching_experience=0):
        self.disciplines = disciplines or []
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.teaching_experience = teaching_experience

    def get_info(self):
        print(f"\nEducator: {self.surname} {self.name} {self.patronymic}")
        print(f"\tYear of birth: {self.year_of_birth}")
        print(f"\tTeaching experience: {self.teaching_experience} years")
        print("\nDisciplines:")
        for i, discipline in enumerate(self.disciplines):
            print(f"\tDiscipline #{i + 1}:")
            discipline.get_info()


def main():
    first_student = Student(surname="Blair", name="Amara", patronymic="Rosalind")
    second_student = BudgetStudent(surname="Stone", name="Cade", patronymic="Oliver", budget=2800.90)
    third_student = Student(surname="Morgan", name="Zara", patronymic="Althea")
    fourth_student = Student(surname="Parks", name="Kyler", patronymic="Emery")
    fifth_student = BudgetStudent(surname="Lowe", name="Sienna", patronymic="Eileen", budget=1980.00)
    group = Group(number=525, students=[first_student, second_student, third_student, fourth_student, fifth_student])
    group.get_info()

    first_discipline = Discipline(name="Computer circuitry", credits_num=4, semester=3)
    second_discipline = Discipline(name="Software systems on a crystal", credits_num=4.5, semester=4)
    educator = Educator(disciplines=[first_discipline, second_discipline], surname="Perepelitsyn", name="Artem",
                        patronymic="Evgenovich", year_of_birth=1985, teaching_experience=12)
    educator.get_info()


if __name__ == "__main__":
    main()
