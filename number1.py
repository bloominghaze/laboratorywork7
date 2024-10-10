employees = {
    "Іванов": (15000, "чоловік"),
    "Петрова": (12000, "жінка"),
    "Сидоров": (18000, "чоловік"),
    "Кузнєцова": (11000, "жінка"),
    "Мельник": (14000, "чоловік"),
    "Смирнова": (11500, "жінка"),
    "Федоров": (19000, "чоловік"),
    "Левченко": (12500, "жінка"),
    "Сергієнко": (16000, "чоловік"),
    "Гончарова": (13000, "жінка")
}

def print_employees(data):
    for surname, (salary, gender) in data.items():
        print(f"Прізвище: {surname}, Зарплата: {salary}, Стать: {gender}")

def add_employee(data):
    surname = input("Введіть прізвище співробітника: ")
    try:
        salary = int(input("Введіть зарплату: "))
        gender = input("Введіть стать (чоловік/жінка): ").lower()
        if gender not in ['чоловік', 'жінка']:
            raise ValueError("Некоректно введена стать. Можна тільки 'чоловік' або 'жінка'.")
        data[surname] = (salary, gender)
        print(f"Запис про співробітника {surname} успішно додано.")
    except ValueError as e:
        print(f"Помилка введення: {e}")

def remove_employee(data):
    surname = input("Введіть прізвище співробітника для видалення: ")
    if surname in data:
        del data[surname]
        print(f"Запис про співробітника {surname} успішно видалено.")
    else:
        print("Помилка: Співробітник з таким прізвищем не знайдений.")

def print_sorted_employees(data):
    for surname in sorted(data.keys()):
        salary, gender = data[surname]
        print(f"Прізвище: {surname}, Зарплата: {salary}, Стать: {gender}")

def highest_salary_employee(data):
    max_salary_employee = max(data.items(), key=lambda item: item[1][0])
    print(f"Найбільша зарплата у співробітника {max_salary_employee[0]}: {max_salary_employee[1][0]} грн")

def lowest_salary_by_gender(data):
    min_male = min((item for item in data.items() if item[1][1] == "чоловік"), key=lambda item: item[1][0])
    min_female = min((item for item in data.items() if item[1][1] == "жінка"), key=lambda item: item[1][0])

    print(f"Чоловік з найменшою зарплатою: {min_male[0]} з зарплатою {min_male[1][0]} грн")
    print(f"Жінка з найменшою зарплатою: {min_female[0]} з зарплатою {min_female[1][0]} грн")

def main():
    while True:
        print("\nМеню:")
        print("1. Вивести всіх співробітників")
        print("2. Додати нового співробітника")
        print("3. Видалити співробітника")
        print("4. Вивести співробітників, відсортованих за прізвищем")
        print("5. Вивести співробітника з найбільшою зарплатою")
        print("6. Вивести чоловіка і жінку з найменшою зарплатою")
        print("7. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            print_employees(employees)
        elif choice == "2":
            add_employee(employees)
        elif choice == "3":
            remove_employee(employees)
        elif choice == "4":
            print_sorted_employees(employees)
        elif choice == "5":
            highest_salary_employee(employees)
        elif choice == "6":
            lowest_salary_by_gender(employees)
        elif choice == "7":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
