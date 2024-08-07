import streamlit as st


def app():
    st.markdown("# About the App 📝")
    st.write("This Data Fetching and Exporting Application is a sophisticated tool designed for seamless integration with Bubble's application database. This application, developed using Streamlit and Python, enables users to fetch and export data efficiently by constructing dynamic API URL endpoints based on user-specified constraints. By leveraging this tool, users can tailor their data retrieval processes to meet specific criteria, ensuring that they receive precisely the data they need for their analysis, reporting, or other data-driven tasks.")

    st.markdown("### 🔑 Key Features")
    st.markdown("1. **User-Friendly Interface**: Leveraging Streamlit's interactive capabilities, the app provides an intuitive interface for users to interact with and specify their data retrieval requirements.")
    st.markdown("2. **Dynamic Data Fetching**: Users can input constraints directly into the app, which are then applied to the API URL endpoint to fetch specific data from the Bubble application database.")
    st.markdown("3. **Flexible Constraints**: The application supports a variety of constraints, enabling users to filter data based on multiple criteria to meet their specific needs.")
    st.markdown("4. **Data Exporting**: Once the data is fetched, users can easily export it in an Excel format (.xlsx), facilitating further analysis or reporting.")
    
    st.markdown("### 📖 Usage")
    st.markdown("1. **Input Constraints**: Users can enter constraints in the designated fields within the app interface. These constraints can include specific fields, conditions, or ranges to filter the desired data.")
    st.markdown("2. **Data Retrieval**: Upon submitting the constraints, the application constructs the appropriate API URL endpoint and retrieves the data from the Bubble database.")
    st.markdown("3. **Data Display**: The retrieved data is displayed within the app, allowing users to review and verify the information.")
    st.markdown("4. **Data Exporting**: Users can export the data in Excel format (.xlsx) for further use or analysis.")
    
    
    st.markdown("### 🛠️ Technical Specification")
    st.markdown("1. **Frontend**: Streamlit framework provides an interactive web-based interface for user inputs and data display.")
    st.markdown("2. **Backend**: Python scripts handle the construction of API URL endpoints based on user-defined constraints and manage data retrieval from the Bubble application database.")
    st.markdown("3. **API Integration**: The application interacts with Bubble's Data API to fetch and filter data based on dynamically generated URL endpoints.")
    
    st.write("\n")
    st.markdown("#### Developer: Kim Emerson M. Tan")
    st.markdown("#### Role: Backend Developer Intern PITX")