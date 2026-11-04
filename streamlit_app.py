import streamlit as st

st.title("My first Streamlit App")
name = st.text_input("Your name:")
if name:
    st.write(f"Hi! {name}！")
