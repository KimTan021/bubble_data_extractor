import streamlit as st
from data_manager import convert_to_excel

def create_excel(data):
    excel_file = convert_to_excel(data)
    st.download_button(label="Download Excel",
                    data=excel_file,
                    file_name="data.xlsx",
                    mime="application/vnd.ms-excel")