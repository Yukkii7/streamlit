import streamlit as st
st.title('My first webapp')


# You have to write a program that determine whether you will accept loan applicaxtion or reject. You will determine acceptence based on annual salary and year of work. Acceptance standard is Annual salary is greater than >= 500,000 yuan, and >= 5 year of work in current work
annual_salary = st.number_input("Enter your annual salary")
year_work = st.number_input("Enter your Year of work")
if st.button("Submit"):
    if annual_salary >= 500000 and year_work >= 5:
        st.write("Your applicxation is accpeted")
    else:
        st.write("Sory your applicxation is not accpeted")

