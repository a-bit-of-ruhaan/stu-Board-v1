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

students = load_students()

APP_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="STUDENT's DASHBOARD",
    layout="wide"
)

with open(APP_DIR / "style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.sidebar.title("Student Hub")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Student Analytics"]
)

st.title("StuBoard")
st.write("A working Dashboard which provides dataframes with feature like Sorting, Filtering and Analyzing")
st.write("Use the navigation bar to switch pages")

if page == "Dashboard":
    col1, col2 = st.columns([4, 1])

    st.markdown(
        """
        <div class="Header_m">
            <h1>DASHBOARD</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.title("STUDENT METRICS OF GIVEN DATA")
        st.write("Navigate to the Analytics page for more detailed info.")

    with col2:
        st.write(" ")

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Total Students", total_students(students))
    with col4:
        st.metric("Average Marks", round(average_marks(students), 2))

    col5, col6 = st.columns(2)
    with col5:
        st.metric("Highest Marks", highest_marks(students))
    with col6:
        st.metric("Lowest Marks", lowest_marks(students))

elif page == "Student Analytics":
    st.title("STUDENT DASHBOARD")

    st.subheader("Search Students")
    search = st.text_input(
        "Search Name",
        placeholder="Enter Name"
    )

    # 1. Start with the search filter
    filtered_students = search_students(students, search)
    
    # --- MOVED ALL FILTER CODE INSIDE THIS BLOCK ---
    colx, coly = st.columns(2)
    with colx:
        city = st.selectbox(
            "City",
            ["All"] + sorted(students["City"].unique().tolist())
        )
        filtered_students = filter_by_city(filtered_students, city)
    with coly:
        student_class = st.selectbox(
            "Class",
            ["All"] + sorted(students["Class"].unique().tolist())
        )
        filtered_students = filter_by_class(filtered_students, student_class)

    marks = st.slider(
        "Minimum Marks",
        0,
        100,
        0
    )
    filtered_students = filter_by_marks(filtered_students, marks)

    cola, colb = st.columns(2)
    with cola:
        sort_column = st.selectbox(
            "Sort By", ["Name", "Age", "Marks"]
        )

    with colb:
        ascending = st.checkbox(
            "Ascending Order"
        )    
        filtered_students = sort_students(filtered_students, sort_column, ascending)

    # 2. Display the final filtered dataframe at the very end
    st.write(f"Showing {len(filtered_students)} students")
    st.dataframe(filtered_students, use_container_width=True, hide_index=True)
