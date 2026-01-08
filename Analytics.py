import pandas as pd


all_subjects_score = [   #Сохраним наименования колонок в одну переменную
    "Math_Score",
    "English_Score",
    "Science_Score"
]


def average_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, добавляющая в датасет целый столбец со средним баллом для каждого студента
    """
    df = df.copy()
    df["AverageScore"] = df[all_subjects_score].mean(axis=1)
    return df


def best_student(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с наилучшей успеваемостью
    """
    max_score = df["AverageScore"].max()
    return df[df["AverageScore"] == max_score]


def worst_student(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с наихудшей успеваемостью
    """
    min_score = df["AverageScore"].min()
    return df[df["AverageScore"] == min_score]


def best_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с наилучшей посещаемостью
    """
    max_attendance = df["Attendance"].max()
    return df[df["Attendance"] == max_attendance]


def worst_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, находящая студента с наихудшей посещаемостью
    """
    min_attendance = df["Attendance"].min()
    return df[df["Attendance"] == min_attendance]

def average_math_score(df):
    """
    Функция, находящая средний балл по математике
    """
    return df["Math_Score"].mean()

def average_english_score(df):
    """
    Функция, находящая средний балл по английскому
    """
    return df["English_Score"].mean()

def average_science_score(df):
    """
    Функция, находящая средний балл по наукам
    """
    return df["Science_Score"].mean()

def find_student(df: pd.DataFrame, student_id: int) -> pd.DataFrame:
    """
    Функция, находящая результаты студента по его айди
    """
    return df[df["StudentID"] == student_id]