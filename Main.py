from DataLoader import data_frame
from Menu import print_head, show_menu, get_choice
from Controller import *


def main():
    print_head()

    df = data_frame("Data/Students.csv")
    df = average_score(df)

    flag = True #флаг для отслеживания работы программы и для выхода при вводе нуля
    while flag:
        show_menu()
        choice = get_choice()
        flag = menu_choice(choice, df)


if __name__ == "__main__":
    main()