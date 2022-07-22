import streamlit as st
import pandas as pd
from sklearn import datasets
import os

st.write("""
# Addition
This app adds 2 numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
  num1 = st.number_input("a",min_value=-10000000.0,max_value=10000000.0)
  num2 = st.number_input("b",min_value=-10000000.0,max_value=10000000.0)

  inps = {
    'a' : num1,
    'b' : num2
    }

  df = pd.DataFrame(inps, index=[0])

  return df

df = user_input_features()
n1 = df.a.iloc[0]
n2 = df.b.iloc[0]

st.header('Output')
st.write('a + b = ',str(n1+n2))