import streamlit as st

st.write("""
# Addition
This app adds 2 numbers
""")

#Get Input

st.header('User Input Parameters')

num1 = st.number_input("a",min_value=-10000000.0,max_value=10000000.0)
num2 = st.number_input("b",min_value=-10000000.0,max_value=10000000.0)

st.header('Output')
st.write('a + b = ',str(num1+num2))
