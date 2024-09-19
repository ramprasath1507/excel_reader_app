import streamlit as st
import pandas as pd

st.title("Excel Reader Calculator App")
uploaded_file = st.file_uploader("Upload your Excel file", type=['xlsx', 'xls']
                                 
df = None

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Preview of uploaded Excel file:")
        st.write(df)
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Run"):
    if df is not None:
        st.write("Processing your Excel data...")
        summary = df.describe()
        st.write("Summary of numeric columns:")
        st.write(summary)
    else:
        st.error("Please upload an Excel file first!")

