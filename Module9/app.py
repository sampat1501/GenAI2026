import streamlit as st
import pandas as pd
import numpy as np

##Application Title
st.title("GenAI2026 Project ")

# Display Simple text
st.text("This is simple text")

# Display dataframe
data = pd.DataFrame(
    {
        "First Column": [10, 20, 30, 40, 50, 60, 60],
        "Second Column": [21, 22, 31, 25, 36, 14, 2],
    }
)


# Display dataframe
st.write("This is dataframe")
st.write(data)

# Create Linechart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)
