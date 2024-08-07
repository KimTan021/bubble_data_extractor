import streamlit as st


def app():
    st.markdown("# About the App 📝")
    st.markdown("**App Name:** Bubble Data Extractor")
    st.markdown(
        "**Developer:** Kim Emerson M. Tan (Backend Developer Intern PITX)")
    
    st.markdown("""
        <p style="text-align: justify;">The Bubble Data Extractor is a sophisticated tool designed for seamless integration with Bubble's application database. This application, developed using Streamlit and Python, enables users to fetch and export data efficiently by constructing dynamic API URL endpoints based on user-specified constraints. By leveraging this tool, users can tailor their data retrieval processes to meet specific criteria, ensuring that they receive precisely the data they need for their analysis, reporting, or other data-driven tasks.</p>
    """, unsafe_allow_html=True)

    st.markdown("#### 🔑 Key Features")
    st.markdown("""
        <p style="text-align: justify;">
        1. <strong>User-Friendly Interface</strong>: Leveraging Streamlit's interactive capabilities, the app provides an intuitive interface for users to interact with and specify their data retrieval requirements.
        </p>
        <p style="text-align: justify;">
        2. <strong>Dynamic Data Fetching</strong>: Users can input constraints directly into the app, which are then applied to the API URL endpoint to fetch specific data from the Bubble application database.
        </p>
        <p style="text-align: justify;">
        3. <strong>Flexible Constraints</strong>: The application supports a variety of constraints, enabling users to filter data based on multiple criteria to meet their specific needs.
        </p>
        <p style="text-align: justify;">
        4. <strong>Data Exporting</strong>: Once the data is fetched, users can easily export it in an Excel format (.xlsx), facilitating further analysis or reporting.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📖 Usage")
    st.markdown("""
        <p style="text-align: justify;">
        1. <strong>Input Constraints</strong>: Users can enter constraints in the designated fields within the app interface. These constraints can include specific fields, conditions, or ranges to filter the desired data.
        </p>
        <p style="text-align: justify;">
        2. <strong>Data Retrieval</strong>: Upon submitting the constraints, the application constructs the appropriate API URL endpoint and retrieves the data from the Bubble database.
        </p>
        <p style="text-align: justify;">
        3. <strong>Data Display</strong>: The retrieved data is displayed within the app, allowing users to review and verify the information.
        </p>
        <p style="text-align: justify;">
        4. <strong>Data Exporting</strong>: Users can export the data in Excel format (.xlsx) for further use or analysis.
        </p>
    """, unsafe_allow_html=True)
    
    
    st.markdown("#### 🛠️ Technical Specification")
    st.markdown("""
        <p style="text-align: justify;">
        1. <strong>Frontend</strong>: Streamlit framework provides an interactive web-based interface for user inputs and data display.
        </p>
        <p style="text-align: justify;">
        2. <strong>Backend</strong>: Python scripts handle the construction of API URL endpoints based on user-defined constraints and manage data retrieval from the Bubble application database.
        </p>
        <p style="text-align: justify;">
        3. <strong>API Integration</strong>: The application interacts with Bubble's Data API to fetch and filter data based on dynamically generated URL endpoints.
        </p>
    """, unsafe_allow_html=True)
    
    
    st.markdown("#### 📄 Pages")
    
    st.markdown("""
        <ul>
            <li><strong>Fetch Data</strong>
                <ul>
                    <li style="text-align: justify;">The <strong>Fetch Data</strong> page is the core functionality of the app, where users input the Data API URL endpoint provided by Bubble. On this page, users can configure constraints to specify exactly what data they wish to retrieve from Bubble’s database. After configuring the constraints, users can initiate the data fetching process. The page provides a clear interface to enter the API URL, set filtering criteria, and view the fetched data in a tabular format.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <ul>
            <li><strong>Documentation</strong>
                <ul>
                    <li style="text-align: justify;">The <strong>Documentation</strong> page provides comprehensive information about the Bubble Data Extractor, including detailed instructions on how to use the app, technical specifications, and examples. This page serves as a reference for users to understand the app’s features, usage procedures, and configuration requirements. It includes sections on how to enter API URLs, apply constraints, and export data, ensuring users can effectively utilize the app's functionalities.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <ul>
            <li><strong>Constraints</strong>
                <ul>
                    <li style="text-align: justify;">The <strong>Constraints</strong> page provides detailed guidance on how to use various constraint types available in Bubble's Data API. This page serves as an informational resource, offering explanations and examples for applying different types of constraints such as field constraints, comparison operators, list constraints, and search constraints. It helps users understand how to configure their data queries effectively but does not include interactive elements for setting constraints directly.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <ul>
            <li><strong>Limitations</strong>
                <ul>
                    <li style="text-align: justify;">The <strong>Limitations</strong> page outlines the constraints and potential issues associated with using the Bubble Data Extractor. This page provides an overview of the limitations related to data size, complexity of constraints, API rate limits, and performance considerations. It helps users understand the boundaries and challenges of the app, ensuring they are aware of any potential impacts on their data retrieval and analysis processes.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <ul>
            <li><strong>About</strong>
                <ul>
                    <li style="text-align: justify;">The <strong>About</strong> page offers a comprehensive overview of the Data Fetcher and Exporter App. It includes key information about the app, such as its features, usage instructions, and technical specifications. Additionally, this page provides details about the app's developer, including its role in the company. The <strong>About</strong> page aims to give users a clear understanding of the app's purpose, capabilities, and development context.</li>
                </ul>
            </li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.write("\n")
    st.markdown("#### 📧 Contact Developer")
    st.markdown("""
        <ul>
            <li><strong>Developer:</strong> Kim Emerson M. Tan</li>
            <li><strong>Email:</strong> <a href="mailto:kmtan@spmadridlaw.com">kmtan@spmadridlaw.com</a></li>
            <li><strong>Github:</strong> <a href="https://github.com/KimTan021">github.com/KimTan021</a></li>
        </ul>
    """, unsafe_allow_html=True)
    