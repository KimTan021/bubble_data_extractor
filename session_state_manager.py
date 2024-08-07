import streamlit as st

def manage_states():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    if 'filters' not in st.session_state:
        st.session_state.filters = []
    
    if 'prev_endpoint' not in st.session_state:
        st.session_state.prev_endpoint = ""

    if 'filtering_done' not in st.session_state:
        st.session_state.filtering_done = False