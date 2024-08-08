import streamlit as st

def manage_states():
    """
    Manages the session states for the application.

    This function checks if the required session states are present and initializes them if not.

    Session States:
    - current_page: The current page number.
    - filters: A list of filters applied.
    - prev_endpoint: The previous endpoint.
    - filtering_done: Indicates if filtering has been done.

    Returns:
    None
    """
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    if 'filters' not in st.session_state:
        st.session_state.filters = []
    
    if 'prev_endpoint' not in st.session_state:
        st.session_state.prev_endpoint = ""

    if 'filtering_done' not in st.session_state:
        st.session_state.filtering_done = False
