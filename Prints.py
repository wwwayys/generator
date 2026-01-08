def print_students(df, value_column):
    """
    Функция, позволяющая удобно выводить инфоормацю о студентах
    """
    for _, row in df.iterrows(): # Проходим по строкам df, используя метод iterrows (индекс обозначаем как "_', так как мы его не используем)
        print(
            f"StudentID {row['StudentID']} — "
            f"{value_column}: {row[value_column]:.2f}" # используем f-строки для вывода и ограничиваем значения до 2 знаков после запятой для удобства
        )


def print_student_info(df):
    """
    Функция для вывода информации о студенте
    """
    if df.empty:
        print("Студент с таким ID не найден.")
        return

    row = df.iloc[0] #с помощью метода iloc находим первую стркоу df (единственного найденного студента)
    print("\nИнформация о студенте:")
    print(f"StudentID: {row['StudentID']}")
    print(f"Средний балл: {row['AverageScore']:.2f}")
    print(f"Посещаемость: {row['Attendance']:.2f}")

def go_back():
    """
    Функция для выхода из интерфейсов
    """
    while True:
        value = input("\nВведите 0 для возврата в меню: ")
        if value == "0":
            return
        print("Неверный ввод.")
