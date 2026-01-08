from Analytics import *
from Menu import subject_menu, get_choice
from Prints import *

def show_subject(df):
    """
    Функция для выбора предметов в интерфейсе
    """
    while True:
        subject_menu()
        choice = get_choice()

        if choice == 0:
            return

        elif choice == 1:
            avg = average_math_score(df)
            print(f"\nСредний балл по математике: {avg:.2f}")
            go_back()

        elif choice == 2:
            avg = average_english_score(df)
            print(f"\nСредний балл по английскому: {avg:.2f}")
            go_back()

        elif choice == 3:
            avg = average_science_score(df)
            print(f"\nСредний балл по наукам: {avg:.2f}")
            go_back()

        else:
            print("Неверный выбор.")
            go_back()


def menu_choice(choice, df):
    """
    функция для выбора необходимой информации в меню
    """
    if choice == 1:
        print("\nСредний балл всех студентов:")
        print_students(df, "AverageScore")
        go_back()

    elif choice == 2:
        print("\nЛучшая успеваемость:")
        print_students(best_student(df), "AverageScore")
        go_back()

    elif choice == 3:
        print("\nХудшая успеваемость:")
        print_students(worst_student(df), "AverageScore")
        go_back()

    elif choice == 4:
        show_subject(df)

    elif choice == 5:
        value = input("Введите StudentID: ")
        if value.isdigit():
            print_student_info(find_student(df, int(value)))
        else:
            print("Некорректный ID.")
        go_back()

    elif choice == 6:
        print("\nЛучшая посещаемость:")
        print_students(best_attendance(df), "Attendance")
        go_back()

    elif choice == 7:
        print("\nХудшая посещаемость:")
        print_students(worst_attendance(df), "Attendance")
        go_back()

    elif choice == 0:
        return False

    else:
        print("Неверный пункт меню.")
        go_back()

    return True
