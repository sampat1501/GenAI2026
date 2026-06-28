import streamlit as st
import pandas as pd

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello Mr. {name}")
age = st.slider("Select your age : ", 0, 100, 25, 1)
st.write(f"Your age is {age}")

options = ["Python", "Java", "JavaScript", "C#Sharp"]
choice = st.selectbox("Choose you favrite option", options)
st.write(f"Your selected option is : {choice}")

# Display dataframe
data = pd.DataFrame(
    {
        "First Column": [10, 20, 30, 40, 50, 60, 60],
        "Second Column": [21, 22, 31, 25, 36, 14, 2],
    }
)
st.write("This is the dataframe")
st.write(data)

uploaded_file = st.file_uploader("Upload any csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
