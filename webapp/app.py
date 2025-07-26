import streamlit as st

st.title("📊 My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app built with Streamlit!")

# Interactive element
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider example
age = st.slider("Select your age", 1, 100, 25)
st.write("You selected:", age)
