
import streamlit as st

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
