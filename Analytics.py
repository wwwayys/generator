import pandas as pd


all_subjects_score = [   #Сохраним наименовния колонок в одну переменную
    "Math_Score",
    "English_Score",
    "Science_Score"
]


def average_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, считающая средний балл студента по всем предметам
    """
    df = df.copy()
    df["AverageScore"] = df[all_subjects_score].mean(axis=1)
    return df


def best_student(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с лучшей успеваемостью
    """
    max_score = df["AverageScore"].max()
    return df[df["AverageScore"] == max_score]


def worst_student(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, назодящая студента с худшей успеваемостью
    """
    min_score = df["AverageScore"].min()
    return df[df["AverageScore"] == min_score]


def best_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с лучшей посещаемостью
    """
    max_attendance = df["Attendance"].max()
    return df[df["Attendance"] == max_attendance]


def worst_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с худшей поссещаемостью
    """
    min_attendance = df["Attendance"].min()
    return df[df["Attendance"] == min_attendance]

