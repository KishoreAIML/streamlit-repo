
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

image = Image.open("https://www.google.com/imgres?q=llms%20interview%20questions&imgurl=https%3A%2F%2Fcdn.analyticsvidhya.com%2Fwp-content%2Fuploads%2F2024%2F10%2FLLMs.webp&imgrefurl=https%3A%2F%2Fwww.analyticsvidhya.com%2Fblog%2F2024%2F04%2Fllm-interview-questions%2F&docid=oXlEYVFgTEH5OM&tbnid=wzCkvLh6fYyjeM&vet=12ahUKEwiZjcTtgvaPAxXiS2wGHdj-I60QM3oECBcQAA..i&w=872&h=490&hcb=2&ved=2ahUKEwiZjcTtgvaPAxXiS2wGHdj-I60QM3oECBcQAA")
st.image(image , width = 200)
