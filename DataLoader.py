import pandas as pd

def data_frame(path: str) -> pd.DataFrame:
    """
    Фукнция, считывающая датасет
    """
    df = pd.read_csv('Data/Students.csv')
    df.insert(0, "StudentID", range(1, len(df) + 1)) # Добавление колонки с айди для каждого студента
    return df