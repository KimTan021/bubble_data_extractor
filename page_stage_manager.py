import streamlit as st
import pandas as pd

def increment_page(total_pages):
    if st.session_state.current_page < total_pages - 1:
        st.session_state.current_page += 1

def decrement_page():
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1
        

def arrange_page(data):
    # Calculate total pages needed
    total_pages = len(data) // 15 + \
        (1 if len(data) % 15 > 0 else 0)

    # Slice data for current page
    start = st.session_state.current_page * 15
    end = start + 15
    page_data = data[start:end]

    page_data_with_index = change_page_indexing(page_data, start)
    
    return page_data_with_index, total_pages


def change_page_indexing(page_data, start=0):
        # Adjust index for continuous counting
    page_data_with_index = pd.DataFrame(
        page_data).reset_index(drop=True)
    page_data_with_index.index = range(
        start + 1, start + len(page_data_with_index) + 1)
    
    return page_data_with_index