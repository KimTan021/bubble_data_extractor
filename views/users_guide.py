import streamlit as st


def app():
    st.markdown("# Users Guide 📖")

    st.markdown("**App Name:** Bubble Data Extractor")
    st.markdown(
        "**Developer:** Kim Emerson M. Tan (Backend Developer Intern PITX)")

    st.write("\n")
    st.markdown("#### ✅ Requirements")
    st.markdown(
        "To effectively use the Bubble Data Extractor, the following requirements must be met:")
    st.markdown("""
        <p style="text-align: justify;">
        1. <strong>Internet Connection:</strong> A stable internet connection is required to access Bubble’s Data API and fetch data from the database. Ensure that your network connection is reliable to avoid interruptions during data retrieval.
        </p>
        <p style="text-align: justify;">
        2. <strong>Bubble Data API URL:</strong> You need to have a valid and properly formatted Bubble Data API URL endpoint. This URL is necessary for connecting to your Bubble application's database and fetching the required data.
        </p>
        <p style="text-align: justify;">
        3. <strong>Browser Compatibility:</strong> The app is designed to work with modern web browsers. Ensure you are using an up-to-date version of browsers such as Google Chrome, Mozilla Firefox, or Microsoft Edge for the best experience.
        </p>
    """, unsafe_allow_html=True)

    st.write("\n")
    st.markdown("#### 📘 How to Use")
    st.markdown("To get started using the app, you first need to access it via this web address: https://bubble-data-extractor.streamlit.app/")

    st.markdown("###### Fetching data from the app")
    st.markdown("""
        <p style="text-align: justify;">1. After accessing the website, you need to put a valid Bubble Data API endpoint (e.g., https://[app name].bubbleapps.io/api/1.1/obj/[data type/data table]) in the text input shown in the image.</p>
    """, unsafe_allow_html=True)
    st.image("images/getting_started.png")
    st.markdown("""
        <p style="text-align: justify;">2. After that, you can filter data by clicking the \"Add Column to Filter\" button, specifying the column you want to filter, the constraint type, and, if necessary, the value you need to filter the column by. If you're done filtering, just click the \"Filtering Done\" button below. For more information on constraint types, go to the **Constraints** tab of the app.</p>
    """, unsafe_allow_html=True)
    st.image("images/filter_column.png")
    st.markdown("- If you don't want to filter the data, you can also just click \"Filtering Done\" to fetch all the data on the endpoint provided.")
    st.image("images/filtering_done.png")

    st.markdown("""
        <ul>
            <li><strong>Things to note when filtering by date:</strong>
                <ul>
                    <li style="text-align: justify;">If you filter by date, the value will change to a date input, and you need to select the date you want to filter your data by. For the date that you selected, for example, 8/7/2024, its hours, minutes, and seconds will all be 0. Basically, it is the very first start of the day.</li>
                    <li style="text-align: justify;">So if you want to filter the data within a specific date range, you need to use "greater than" and "less than" as your constraint types. Basically, you filter by two columns with the same name (e.g., Created Date) to filter the data with a specific date range.</li>
                    <li style="text-align: justify;">For example, if you want to filter data from January 1, 2024, to May 31, 2024, you will first add a column, such as "Created Date." Select "greater than" as the constraint type and input January 1, 2024. Next, add another column, choose "less than" as the constraint type, and input June 1, 2024, instead of May 31, 2024. This is because the time for the date will default to 0, so inputting June 1 ensures that data for May 31 is included. Essentially, inputting the day after your end date covers all data up to and including May 31.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <ul>
            <li><strong>Things to note when filtering by number:</strong>
                <ul>
                    <li style="text-align: justify;">When writing a number as a value, don't use a comma (,) to separate digits. This is to avoid not filtering the data you want, just use the normal format of a number without any commas.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style="text-align: justify;">3. When you click the \"Filtering Done\" button, the data you requested will be fetched from Bubble's application database, and this process might take some time depending on the amount of data being fetched from the database. To know more about the limitations of Bubble, go to the \"Limitations\" tab of the app.</p>
    """, unsafe_allow_html=True)
    st.image("images/data_results.png")
    st.markdown("""
        <p style="text-align: justify;">4. After the data has been fetched, there will be a \"Download Excel\" button below the \"Filtering Done\" button you can click in order to download the data in Excel format.</p>
    """, unsafe_allow_html=True)
    st.image("images/download_excel.png")
    st.markdown("""
        <p style="text-align: justify;">5. Lastly, the final URL endpoint is shown every time you add a URL endpoint or add columns to filter. This is purposely done for you to also check the response being received by the app. You can click on the URL being generated to check the response.</p>
    """, unsafe_allow_html=True)
    st.image("images/final_url.png")
    