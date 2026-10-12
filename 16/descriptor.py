class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return 65 - instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 18:
            raise ValueError("Вік не може бути менше 18 років")

        instance.__dict__[self.name] = value


class SalaryDescriptor:
    MIN_SALARY = 1000

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        salary = instance.__dict__[self.name]
        return salary * 0.8

    def __set__(self, instance, value):
        if value < self.MIN_SALARY:
            raise ValueError(
                f"Зарплатня не може бути менше {self.MIN_SALARY} доларів"
            )

        instance.__dict__[self.name] = value


class User:
    age = AgeDescriptor()
    salary = SalaryDescriptor()

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get(self):
        return {
            "name": self.name,
            "years_to_retirement": self.age,
            "salary_after_tax": self.salary
        }


user = User("Ivan", 18, 900)

print(user.name)
print(user.age)
print(user.salary)

print(user.get())
