
import streamlit as st
from PIL import Image

st.title("Hellow World!")
st.header("This is a header") 

st.subheader("This is a subheader")
st.text("Hello GeeksForGeeks!!!")
st.markdown("This is markdown")
st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

image = Image.open("C:\Users\KISHORE\OneDrive\Pictures\Documents\skills\Python\numpyExcercise\.venv\Lib\site-packages\matplotlib\mpl-data\sample_data\grace_hopper.jpg")
st.image(image , width = 200)

