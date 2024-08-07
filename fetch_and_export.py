import pandas as pd
import streamlit as st
from data_manager import fetch_data, get_columns, get_constraints, requires_value, popFilter
from session_state_manager import manage_states
from page_stage_manager import increment_page, decrement_page, arrange_page
from create_excel import create_excel
import json
from urllib.parse import quote
from datetime import datetime

# st.title("Data Fetching and Exporting")
def app():

    manage_states()

    st.markdown("##### Overview")
    st.write("This Bubble Data Extractor is a robust tool designed to streamline the process of retrieving and exporting data from a Bubble application database. Utilizing Streamlit and Python, this app offers an intuitive interface for users to fetch data by dynamically generating API URL endpoints based on user-specified constraints. This allows for precise and efficient data retrieval tailored to specific needs.")
    
    st.markdown("##### Enter an endpoint to get started")
    endpoint = st.text_input("Enter an endpoint (e.g., https://your-app-name.bubbleapps.io/api/1.1/obj/your-data-type)")

    if endpoint != st.session_state.prev_endpoint:
        # Clear session state variables to trigger rerun
        st.session_state.filters = []
        st.session_state.filtering_done = False
        st.session_state.prev_endpoint = endpoint
        st.rerun()

    if endpoint:
        column_info = get_columns(endpoint)

        if column_info is None:
            return
        else:
            column_names = list(column_info.keys())

            if column_names:

                # Column filter UI
                st.write("#### Filter Data by Column")

                fil1, fil2, fil3, fil4 = st.columns(4)

                # Limit the number of filters to the number of available columns
                if len(st.session_state.filters) < len(column_names):
                    with fil1:
                        if st.button("Add Column to Filter", on_click=lambda: setattr(st.session_state, 'filtering_done', False)):
                            st.session_state.filters.append(
                                {"column": None, "constraint": None, "value": None})
                            st.rerun()
                    with fil2:
                        st.write("###### ⬅ Click to add a column to filter")

                for i, filter in enumerate(st.session_state.filters):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        default_index = column_names.index(
                            filter["column"]) if filter["column"] else 0
                        new_column = st.selectbox(
                            f"Column {i+1}", column_names, index=default_index, key=f"column_{i}")
                        if new_column != filter["column"]:
                            filter["column"] = new_column
                            st.session_state.filtering_done = False
                            filter["value"] = None
                            st.rerun()
                    with col2:
                        if filter["column"]:
                            data_type = column_info[filter["column"]]
                            constraints = get_constraints(data_type)
                            default_constraint_index = constraints.index(
                                filter["constraint"]) if filter["constraint"] in constraints else 0
                            new_constraint = st.selectbox(f"Constraint {
                                                          i+1}", constraints, index=default_constraint_index, key=f"constraint_{i}")
                            if new_constraint != filter["constraint"]:
                                filter["constraint"] = new_constraint
                                st.session_state.filtering_done = False
                                filter["value"] = None
                                st.rerun()
                    with col3:
                        if filter["column"]:
                            if requires_value(filter["constraint"]):
                                if data_type == "datetime":
                                    if filter["value"] is not None and isinstance(filter["value"], str):
                                        filter["value"] = datetime.strptime(
                                            filter["value"], "%Y-%m-%dT%H:%M:%SZ").date()
                                    new_value = st.date_input(
                                        f"Value {i+1}", value=filter["value"] if filter["value"] else None)
                                    if new_value != filter["value"]:
                                        filter["value"] = new_value
                                        st.session_state.filtering_done = False
                                        st.rerun()
                                else:
                                    new_value = st.text_input(
                                        f"Value {i+1}", value=filter["value"] if filter["value"] else "")
                                    if new_value != filter["value"]:
                                        filter["value"] = new_value
                                        st.rerun()
                    with col4:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.button(f"Remove", key=f"remove_{
                                  i}", on_click=popFilter, args=(i,))

                # Construct the URL endpoint with constraints
                # print(f"Filters: {st.session_state.filters}")
                if st.session_state.filters:
                    constraints = []
                    for filter in st.session_state.filters:
                        if filter["column"] and filter["constraint"]:
                            if filter["value"]:
                                filter["value"] = filter["value"].strftime(
                                    "%Y-%m-%dT00:00:00Z") if column_info[filter["column"]] == "datetime" else filter["value"]
                                constraint = {
                                    "key": filter["column"],
                                    "constraint_type": filter["constraint"],
                                    "value": filter["value"]
                                }
                            else:
                                constraint = {
                                    "key": filter["column"],
                                    "constraint_type": filter["constraint"],
                                }
                            constraints.append(constraint)

                    # print(f"Constraints: {constraints}")
                    if constraints:  # Check if there are any valid constraints
                        constraints_str = json.dumps(constraints)
                        encoded_constraints = quote(constraints_str)
                        final_url = f"{endpoint}?constraints={
                            encoded_constraints}"
                    else:
                        final_url = endpoint
                else:
                    final_url = endpoint

                dn1, dn2, dn3, dn4 = st.columns(4)
                with dn1:
                    done = st.button("Filtering Done", on_click=lambda: setattr(
                        st.session_state, 'filtering_done', True))
                with dn2:
                    st.write("###### ⬅ Click when done filtering")

                if st.session_state.filtering_done:
                    data = fetch_data(final_url)

                    # Convert data to a DataFrame if it's not already one
                    if not isinstance(data, pd.DataFrame):
                        data = pd.DataFrame(data)

                    if data.empty:
                        st.write("No data available.")
                    else:
                        create_excel(data)
                        st.write(f"Search Results: {len(data)} data found.")

                        page_data_with_index, total_pages = arrange_page(data)
                        st.dataframe(page_data_with_index)

                        if len(data) > 15:
                            col1, col2 = st.columns(2)
                            with col1:
                                st.button("Previous", on_click=decrement_page)
                            with col2:
                                st.button(
                                    "Next", on_click=increment_page, args=(total_pages,))

                st.write("### Final URL Endpoint")
                st.write(f"GET {final_url}")

if __name__ == "__main__":
    app()