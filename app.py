import streamlit as st
from pathlib import Path

from functions.std_data import (
    load_students,
    search_students,
    filter_by_city,
    filter_by_class,
    filter_by_marks,
    sort_students,
    average_marks,
    highest_marks,
    lowest_marks,
    total_students
)

APP_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="STUDENT's DASHBOARD",
    layout="wide"
)

with open(APP_DIR / "style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

students = load_students()

st.sidebar.title("Students Hub")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Students", "Analytics"]
)

if page == "Dashboard":

    st.title("STUDENT DASHBOARD")
    st.write("Welcome to the Students Analytics Dashboard")

    st.header("Dashboard")
    st.write("Overview of Students Performance.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Students", total_students(students))

    with col2:
        st.metric("Average Marks", round(average_marks(students), 2))

    with col3:
        st.metric("Highest Marks", highest_marks(students))

    with col4:
        st.metric("Lowest Marks", lowest_marks(students))

elif page == "Students":

    st.title("Students")
    st.write("STUDENT DASHBOARD")

    st.subheader("Search Student")

    search = st.text_input(
        "Search Students",
        placeholder="Enter Student Name"
    )

    filtered_students = search_students(students, search)

    col1, col2 = st.columns(2)

    with col1:
        city = st.selectbox(
            "City",
            ["All"] + sorted(students["City"].unique().tolist())
        )
        filtered_students = filter_by_city(filtered_students, city)

    with col2:
        student_class = st.selectbox(
            "Class",
            ["All"] + sorted(students["Class"].unique().tolist())
        )
        filtered_students = filter_by_class(filtered_students, student_class)

    marks = st.slider("Minimum Marks", 0, 100, 0)
    filtered_students = filter_by_marks(filtered_students, marks)

    col1, col2 = st.columns(2)

    with col1:
        sort_column = st.selectbox("Sort By", ["Name", "Age", "Marks"])

    with col2:
        ascending = st.checkbox("Ascending Order")

    filtered_students = sort_students(filtered_students, sort_column, ascending)

    st.write(f"Showing {len(filtered_students)} students")

    st.dataframe(filtered_students, use_container_width=True, hide_index=True)

elif page == "Analytics":

    st.title("Analytics")
    st.write("Students performance analytics will appear here.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Marks", round(average_marks(students), 2))

    with col2:
        st.metric("Highest Marks", highest_marks(students))

    with col3:
        st.metric("Lowest Marks", lowest_marks(students))
