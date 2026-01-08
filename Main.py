from DataLoader import data_frame
from Analytics import average_score
from Analytics import best_student
from Analytics import worst_student
from Analytics import best_attendance
from Analytics import worst_attendance


def print_head():
    print("=" * 50)
    print("          УСПЕВАЕМОСТЬ НАШИХ СТУДЕНТОВ")
    print("=" * 50)


def print_students(title, df, value_column):
    print(f"\n{title}:")
    for _, row in df.iterrows():
        print(
            f"  StudentID {row['StudentID']} — "
            f"{value_column}: {row[value_column]:.2f}"
        )


def main():
    print_head()

    df = data_frame("Data/Students.csv")
    df = average_score(df)

    print_students("Лучший студент", best_student(df), "AverageScore")
    print_students("Худший студент", worst_student(df), "AverageScore")

    print_students("Студент с лучшей посещаемостью",best_attendance(df),"Attendance")

    print_students("Студент с худшей посещаемостью", worst_attendance(df),"Attendance" )

    print_students("Средний балл каждого студента", df, "AverageScore")


if __name__ == "__main__":
    main()
