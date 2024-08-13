import streamlit as st


def app():
    st.markdown("# Limitations ⚠️")
    st.markdown("##### Overview")
    st.markdown("""
        <p style="text-align: justify;">Bubble is a powerful no-code platform that enables users to build complex web applications without traditional programming. However, despite its many strengths, there are certain limitations to consider when using Bubble.</p>
    """, unsafe_allow_html=True)

    st.markdown("##### Limitations")
    st.markdown("""
        <ul>
            <li style="text-align: justify;">
                You can only get 100 rows of data per API call.
            </li>
            <li style="text-align: justify;">
                There is a limit of 50,000 items in any GET request, meaning that if a database contains 100,000 items and the cursor is set at 50,001 no results will be returned.
            </li>
            <li style="text-align: justify;">
                For the Enterprise plan the limit is 10,000,000 items.
            </li>
            <li style="text-align: justify;">
                The URL endpoint you will use in the app to extract data is limited to Bubble's Data API endpoints. The main reason for this limitation is that different API calls have their own methods of sending data, specifically the JSON data they transmit. As a result, the code is designed to accept data formatted according to how Bubble sends their data using their API.
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("For more information on limitations, please refer to the [Bubble API documentation](https://bubble.io/reference#API.get_api_data).") 