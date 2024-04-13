import random


salary = int(input('Enter your salary '))
bool_elements = [True, False]
bonus = random.choice(bool_elements)


def salary_calculating(salary_variable, bonus_variable):
    if bonus_variable:
        salary_variable = salary_variable + random.randint(0, salary_variable)
    return salary_variable


print(f" '${salary_calculating(salary, bonus)}'")
