import streamlit as st


def app():
    st.markdown("# Developers Guide 💻")

    st.write("\n")
    st.markdown("#### ✅ Requirements")
    st.markdown("- A command line interface or terminal where you can type commands.")
    st.markdown("- An IDE (Integrated Development Environment) or any editor where you can run python applications.")
    
    st.write("\n")
    st.markdown("##### How to Run the App Locally")
    st.markdown("**Note:** In this guide, I will use VS Code as my code editor and the set-up for other editors might be different from this. I prefer you to use the same editor as I have, but if you know how to set-up the Python environment for your editor of choice, then you can freely do that.")
    st.markdown("1. Choose the location where you want to store the app. You can do this by changing directory (cd) to your command line to locate where you want to put the app's files.")
    st.markdown("- **Sample:**")
    st.markdown("""
        ```bash 
        cd Users/SPM/Desktop/Kim-Intern/
        ```
    """)
    st.markdown("- You can also just create a folder where you want to store the app. You can use the command shown below.")
    st.markdown("""
        ```bash 
        mkdir [folder name]
        ```
    """)
    st.markdown("2. After that, you can now clone the app in the remote repository on github (https://github.com/KimTan021/bubble_data_extractor.git) and type the command in the image on the terminal.")
    st.markdown("""
        ```bash 
        git clone https://github.com/KimTan021/bubble_data_extractor.git
        ```
    """)
    st.markdown("- The files of the app will be downloaded at the location where you put it in.")
    st.markdown("3. Open the app in the editor of your choice.")
    st.markdown("4. Set-up the Python environment")
    st.markdown("- To create a python environment for the app, run the command below on your terminal. If you are using VS Code, you can also click on \"Terminal\" on the navigation bar and click \"New Terminal\".")
    st.markdown("""
        ```bash 
        python -m venv .venv
        ```
    """)
    st.markdown("- After the environment has been created, run the command below to cd (change directory) over to the .venv file created")
    st.markdown("""
        ```bash 
        cd .venv
        ```
    """)
    st.markdown("- cd over to the Scripts folder")
    st.markdown("""
        ```bash 
        cd Scripts
        ```
    """)
    st.markdown("- Then, type \"activate\"")
    st.markdown("""
        ```bash 
        activate
        ```
    """)
    st.markdown("- After that, you will see \"(.venv)\" on the left side of your directory like in the example shown below.")
    st.markdown("""
        ```bash 
        (.venv) C:\\Users\\Python-Projects
        ```
    """)
    st.markdown("5. Go back to your main directory or the folder you created to store the app's files, then run \"pip install -r requirements.txt\"")
    st.markdown("""
        ```bash 
        pip install -r requirements.txt
        ```
    """)
    st.markdown("- This will install all the dependencies and packages you need to run the app.")
    st.markdown("6. To run the app, just type \"streamlit run app.py\" on the command line or terminal.")
    st.markdown("""
        ```bash 
        streamlit run app.py
        ```
    """)
    st.markdown("7. The app will open to your default web browser.")
    st.image("images/bubble_data_extractor.png")
    