import streamlit as st
from data_manager import convert_to_excel

def create_excel(data):
    """
    Converts the given data into an Excel file and provides a download button to download the file.

    Args:
        data: The data to be converted into an Excel file.

    Returns:
        None
    """
    excel_file = convert_to_excel(data)
    st.download_button(label="Download Excel",
                    data=excel_file,
                    file_name="data.xlsx",
                    mime="application/vnd.ms-excel")
