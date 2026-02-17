import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title("My First Streamlit App")
st.write("Hello Sharvari")
st.text("Lets start")

name = st.text_input("Enter name: ")

if st.button("Greet"):
    st.success(f"Hello, {name}!")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")

st.image("https://tse4.mm.bing.net/th/id/OIP.gRs_qZQgQGJtFRxbBZG8OwHaEX?pid=Api&P=0&h=250", caption="Sample Image")

st.video("https://youtu.be/D1eL1EnxXXQ?si=9RovNbtYFbJA5PD3")

upload_file = st.file_uploader("Upload a CSV", type='csv')

if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)
st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details...")
option = st.radio("Choose view", ["Show Chart", "Show Table"])

if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")
col1, col2 = st.columns(2)

with col1:
    st.button("Press me in Column 1")

with col2:
    st.button("Press me in Column 2")
with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

st.pyplot(fig)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

st.plotly_chart(fig)
