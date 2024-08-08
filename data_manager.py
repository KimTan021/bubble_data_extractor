import requests
import pandas as pd
import streamlit as st
from io import BytesIO
from dateutil.parser import parse
import re

@st.cache_data
def fetch_data(endpoint):
    """
    Fetches data from the specified API endpoint.

    Parameters:
    endpoint (str): The URL endpoint to fetch data from.

    Returns:
    list: A list of fetched data.

    Raises:
    None

    """
    base_url = f"{endpoint}"
    base_url = requests.utils.requote_uri(base_url)
    all_data = []
    cursor = 0
    
    while True:
        response = requests.get(base_url, params={"cursor": cursor})
        if response.status_code == 200:
            data = response.json()["response"]["results"]
            
            if response.json()["response"]["count"] == 0:
                all_data.extend(data)
                break
            else:
                all_data.extend(data)
                cursor += response.json()["response"]["count"]
                
            # print(f"Fetched {response.json()["response"]["count"]} Remaining: {response.json()['response']['remaining']}")
        else:
            print(f"Failed to fetch data, status code: {response.status_code}")
            break
    
    return all_data


@st.cache_data
def get_columns(endpoint):
    """
    Retrieves the column names and data types from a Bubble Data API endpoint.

    Args:
        endpoint (str): The URL of the Bubble Data API endpoint.

    Returns:
        dict: A dictionary mapping column names to their corresponding data types.
              If the URL is not a valid Bubble Data API endpoint, returns None.
    """
    base_url = f"{endpoint}"
    base_url = requests.utils.requote_uri(base_url)
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        data = response.json()
        if "response" in data and "results" in data["response"] and len(data["response"]["results"]) > 0:
            columns_info = data["response"]["results"][0]
            columns_data_types = {}
            
            # Regular expression to match the date format "Dec 8, 2023 2:41 pm"
            date_pattern = re.compile(
                r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'
            )
            
            for key, value in columns_info.items():
                if isinstance(value, str) and date_pattern.match(value):
                    try:
                        # Attempt to parse the value as a date
                        parsed_date = parse(value)
                        columns_data_types[key] = 'datetime'
                    except (ValueError, TypeError):
                        # If parsing fails, use the original data type
                        columns_data_types[key] = 'str'
                else:
                    columns_data_types[key] = type(value).__name__
            
            return columns_data_types
        else:
            st.write("The url is not a valid Bubble Data API endpoint.")
            return None
    except (requests.exceptions.RequestException, ValueError):
        st.write("The URL is not a valid Bubble Data API endpoint.")
        return None
    
    
def convert_to_excel(data):
    """
    Converts a given data into an Excel file and returns the file as a BytesIO object.

    Parameters:
    - data: The data to be converted into Excel format.

    Returns:
    - output: A BytesIO object containing the Excel file.

    Example usage:
    data = [['Name', 'Age'], ['John', 25], ['Jane', 30]]
    excel_file = convert_to_excel(data)
    """

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
        worksheet = writer.sheets['Sheet1']

        # adjust column widths based on the length of the data
        for i, column in enumerate(df.columns):
            column_width = max(df[column].astype(
                str).map(len).max(), len(column))
            worksheet.set_column(i, i, column_width)

    output.seek(0)
    return output

def get_constraints(data_type):
    """
    Returns a list of constraints based on the given data type.

    Parameters:
    - data_type (str): The data type for which constraints are needed.

    Returns:
    - constraints (list): A list of constraints based on the given data type.
    """

    all_field_types = ["equals", "not equal", "is_empty", "is_not_empty", "in", "not in"]
    text_fields_types = ["text contains", "not text contains"]
    text_number_date_types = ["greater than", "less than"]
    list_fields_types = ["contains", "not contains", "empty", "not empty"]
    every_single_field_types = all_field_types + text_fields_types + text_number_date_types + list_fields_types
    
    if data_type == "str":
        return all_field_types + text_fields_types
    elif data_type == "int" or data_type == "float" or data_type == "datetime":
        return all_field_types + text_number_date_types
    elif data_type == "list":
        return all_field_types + list_fields_types
    else:
        return every_single_field_types
    
def requires_value(constraint):
    """
    Checks if a constraint requires a value.

    Args:
        constraint (str): The constraint to check.

    Returns:
        bool: True if the constraint requires a value, False otherwise.
    """
    no_value_constraints = ["is_empty", "is_not_empty", "empty", "not empty"]
    return constraint not in no_value_constraints

def popFilter(index):
    """
    Removes a filter from the list of filters in the session state.

    Parameters:
        index (int): The index of the filter to be removed.

    Returns:
        None
    """
    st.session_state.filters.pop(index)
    st.session_state.filtering_done = False
