import streamlit as st
import pandas as pd


def app():
    st.markdown("# Constraints 🚧")
    st.markdown("##### Overview")
    st.markdown("""
        <p style="text-align: justify;">Constraints in Bubble's Data API allow users to filter data based on specific criteria. By applying constraints, you can retrieve only the data that matches your requirements. Constraints are specified in the API request URL and can be combined to form complex queries.</p>
    """, unsafe_allow_html=True)

    # Create a table using streamlit
    data = {
        'Constraint Type': ["equals or not equal", "is_empty or is_not_empty", 
                            "text contains or not text contains", "greater than or less than", 
                            "in or not in", "contains or not contains", "empty or not empty",
                            ],
        'Description': ["Use to test strict equality", "Use to test whether a thing's given field is empty or not",
                        "Use to test whether a text field contains a string. Text contains will not respect partial words that are not of the same stem.",
                        "Use to compare a thing's field value relative to a given value",
                        "Use to test whether a thing's field is in a list or not for all field types.",
                        "Use to test whether a list field contains an entry or not for list fields only.",
                        "Use to test whether a list field is empty or not for list fields only.",
                        ],
        'Field Types': ["All field types", "All field types", "Text fields only", "Text, number, and date fields", 
                       "All field types", "List fields only", "List fields only"]
    }


    df = pd.DataFrame(data)
    st.markdown("##### Constraint Types")
    st.table(df)
    
    st.markdown("For more information on constraints, please refer to the [Bubble API documentation](https://bubble.io/reference#API.get_api_data).")
