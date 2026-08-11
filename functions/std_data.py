import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent


# Load student data
def load_students():
    return pd.read_csv(DATA_DIR / "data" / "students.csv")


# Search students by name
def search_students(df, search):
    if search == "":
        return df

    return df[
        df["Name"].str.contains(search, case=False, na=False)
    ]


# Filter by city
def filter_by_city(df, city):
    if city == "All":
        return df

    return df[df["City"] == city]


# Filter by class
def filter_by_class(df, student_class):
    if student_class == "All":
        return df

    return df[df["Class"] == student_class]


# Filter by marks
def filter_by_marks(df, marks):
    return df[df["Marks"] >= marks]


# Sort students
def sort_students(df, column, ascending=True):
    return df.sort_values(
        by=column,
        ascending=ascending
    )


# Get average marks
def average_marks(df):
    return df["Marks"].mean()


# Get highest marks
def highest_marks(df):
    return df["Marks"].max()


# Get lowest marks
def lowest_marks(df):
    return df["Marks"].min()


# Get total number of students
def total_students(df):
    return len(df)