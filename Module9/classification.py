import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names


df, target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df["species"])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    min_value=float(df["sepal length (cm)"].min()),
    max_value=float(df["sepal length (cm)"].max()),
    value=float(df["sepal length (cm)"].mean()),
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    min_value=float(df["sepal width (cm)"].min()),
    max_value=float(df["sepal width (cm)"].max()),
    value=float(df["sepal width (cm)"].mean()),
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    min_value=float(df["petal length (cm)"].min()),
    max_value=float(df["petal length (cm)"].max()),
    value=float(df["petal length (cm)"].mean()),
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    min_value=float(df["petal width (cm)"].min()),
    max_value=float(df["petal width (cm)"].max()),
    value=float(df["petal width (cm)"].mean()),
)
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)

##Prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

st.write(prediction)
st.write(f"The Predicted species is : {predicted_species}")
