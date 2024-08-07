import pandas as pd
import streamlit as st
from data_manager import fetch_data, fetch_data_types, search_data
from session_state_manager import manage_states
from page_stage_manager import increment_page, decrement_page, arrange_page, change_page_indexing
from create_excel import create_excel
from ui_config import sort_data, date_range_filter

st.set_page_config(page_title="Data Fetching and Exporting")
st.title("Data Fetching and Exporting")

st.write("**Things to note for when using this service:**")
st.write("1. If you want to filter data by columns, you need to remove 'All' from the selected columns.")
st.write("2. Search results or data you got from the first filtering will be the one to be used if you want to filter by another column.")
st.write("3. If you want to search again from the full dataset, you need to click the 'Reset Search' button.")
st.write("4. If you encounter any issue, just click the 'Reset Search' button.")


def main():

    manage_states()

    data_types = fetch_data_types()
    data_types = [" "] + data_types 
    selected_data_type = st.selectbox("Select a data type", options=data_types, index=0)
    if " " in selected_data_type:
        selected_data_type = selected_data_type.replace(" ", "%20")
        
    
    data = fetch_data(selected_data_type)
    
    # Convert data to a DataFrame if it's not already one
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)
    
    if 'filtered_data' not in st.session_state:
        st.session_state.filtered_data = data
    
    if selected_data_type == "%20":
        st.write("Please select a data type you want to view the data.")
    elif data.empty:
        st.write("No data available.")
    else:
        st.session_state.selected_columns = data.columns.tolist()
        selected_columns = st.multiselect('Select columns to display', options=data.columns.tolist(
        ), default=st.session_state.selected_columns)

        # Update session state
        st.session_state.selected_columns = selected_columns
        
        # column names list
        column_names = ["All"] + data.columns.tolist()
    

        # Search functionality
        with st.form("search_form"):
            # Use the counter as part of the key for the text input widget
            st.session_state.search_query = st.text_input("Search data:").strip()
            # Submit button for the form
            search_columns = st.multiselect("Select columns to search in:", column_names, default=["All"])
            
            col1, col2 = st.columns(2)
            with col1:
                submit_button = st.form_submit_button("Search")
            with col2:
                reset_button = st.form_submit_button("Reset Search")
        
        # Reset search or start a new search from the full dataset if needed
        if reset_button:
            st.session_state.current_page = 0   
            st.session_state.search_query = None
            st.session_state.filtered_data = data
            st.session_state.initial_search_done = False
            st.session_state.selected_columns = data.columns.tolist()    

        # Filter data based on search query
        if "All" not in search_columns and st.session_state.search_query:
            
            data_to_search = data if not st.session_state.initial_search_done else st.session_state.filtered_data
            
            if data_to_search.empty:
                data = search_data(data, st.session_state.search_query)
                st.session_state.filtered_data = data[st.session_state.selected_columns]
            else:
                # Dynamically create a mask for filtering rows based on the search query across selected columns
                mask = pd.Series([False] * len(data_to_search), index=data_to_search.index)
                for column in search_columns:
                    mask |= data_to_search[column].astype(str).str.contains(st.session_state.search_query, case=False, na=False)
                
                st.session_state.search_results = data_to_search[mask]
                st.session_state.filtered_data = st.session_state.search_results[st.session_state.selected_columns]
            
            st.session_state.initial_search_done = True
                
            
        elif st.session_state.search_query:
            data = search_data(data, st.session_state.search_query)
            
            if not data.empty:
                st.session_state.initial_search_done = True
            # Filter columns after search
            st.session_state.filtered_data = data[st.session_state.selected_columns]
            
        else:
            # Filter columns for the full dataset
            st.session_state.filtered_data = data[st.session_state.selected_columns]
        
        # Sort data based on column and order
        sort_column, sort_order = sort_data()
            
        # Date range filter
        start_date, end_date = date_range_filter()
        
        # Convert Created Date to timezone-naive
        st.session_state.filtered_data["Created Date"] = pd.to_datetime(st.session_state.filtered_data["Created Date"]).dt.tz_localize(None)

        # Filter data based on date range if both dates are provided
        if start_date and end_date:
            # make the end date cover the entire day
            end_date = end_date + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
            st.session_state.filtered_data = st.session_state.filtered_data[(st.session_state.filtered_data["Created Date"] >= pd.to_datetime(start_date)) & (st.session_state.filtered_data["Created Date"] <= pd.to_datetime(end_date))]
            st.session_state.initial_search_done = True
            
        if sort_order == "Ascending":
            st.session_state.filtered_data = st.session_state.filtered_data.sort_values(by=sort_column, ascending=True)
        else:
            st.session_state.filtered_data = st.session_state.filtered_data.sort_values(by=sort_column, ascending=False)

        # Download button for the filtered dataset
        create_excel(st.session_state.filtered_data, selected_data_type)

        st.write(f"Search Results: {len(st.session_state.filtered_data)} data found.")
        
        page_data_with_index, total_pages = arrange_page(st.session_state.filtered_data)
        
        st.dataframe(page_data_with_index)

        if len(st.session_state.filtered_data) > 15:
            col1, col2 = st.columns(2)
            with col1:
                st.button('Previous', on_click=decrement_page)
            with col2:
                st.button('Next', on_click=increment_page, args=(total_pages,))

if __name__ == "__main__":
    main()
