
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

image = Image.open("go.png")
st.image(image , width = 200)

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")


status = st.radio("Select Gender:" , ["Male" , "Female"])
if status == "Male":
    st.success("Male")
else:
    st.success("Female")



