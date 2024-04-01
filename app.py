import streamlitlit as st

def addition(a,b):
    return(a+b)
st.title("Little Calculator")
a = st.number_input("Enter a first number")
b = st.number_input("Enter a second number")

answer = addition(a,b)
st,write(answer)
