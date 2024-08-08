import streamlit as st
import pandas as pd

def increment_page(total_pages):
    """
    Increments the current page by 1 if it is less than the total number of pages minus 1.

    Parameters:
    total_pages (int): The total number of pages.

    Returns:
    None
    """
    if st.session_state.current_page < total_pages - 1:
        st.session_state.current_page += 1

def decrement_page():
    """
    Decrements the current page number by 1 if it is greater than 0.

    This function is used to navigate to the previous page in a pagination system.

    Parameters:
        None

    Returns:
        None
    """
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1
        

def arrange_page(data):
    """
    Arrange the data into pages and calculate the total number of pages needed.

    Parameters:
    data (list): The data to be arranged into pages.

    Returns:
    tuple: A tuple containing the page data with indexing and the total number of pages.
    """

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
     """
     Adjusts the index of the given page_data DataFrame for continuous counting.

     Parameters:
     - page_data (pandas.DataFrame): The DataFrame containing the page data.
     - start (int): The starting index for the adjusted index. Default is 0.

     Returns:
     - page_data_with_index (pandas.DataFrame): The DataFrame with adjusted index.

     Example:
     >>> data = pd.DataFrame({'Page': ['A', 'B', 'C']})
     >>> change_page_indexing(data, start=1)
         Page
     1     A
     2     B
     3     C
     """
     page_data_with_index = pd.DataFrame(page_data).reset_index(drop=True)
     page_data_with_index.index = range(start + 1, start + len(page_data_with_index) + 1)
     
     return page_data_with_index
