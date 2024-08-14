import hmac
import streamlit as st
import fetch_and_export
from views import users_guide, developers_guide, constraints, limitations, about, chatbot

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """
        Renders the login form for the Bubble Data Extractor application.

        This function displays a login form using Streamlit's `st.form` API.
        Users are prompted to enter their username and password to log in.
        Upon submitting the form, the `password_entered` function is called.

        Returns:
            None
        """
        st.title("🚀 Bubble Data Extractor")
        st.markdown("#### About the App")

        st.markdown("""
            <p style="text-align: justify;">The Bubble Data Extractor is a sophisticated tool designed for seamless integration with Bubble's application database. This application, developed using Streamlit and Python, enables users to fetch and export data efficiently by constructing dynamic API URL endpoints based on user-specified constraints. By leveraging this tool, users can tailor their data retrieval processes to meet specific criteria, ensuring that they receive precisely the data they need for their analysis, reporting, or other data-driven tasks.</p>
        """, unsafe_allow_html=True)
        
        st.markdown("**Please log in to continue.**")
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
            

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()


st.set_page_config(page_title="Bubble Data Extractor", page_icon="🚀")
st.title("🚀 Bubble Data Extractor")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Fetch Data", "Users Guide", "Developers Guide", "Constraints", "Limitations", "About", "Chatbot"])

with tab1:
    fetch_and_export.app()
with tab2:
    users_guide.app()
with tab3:
    developers_guide.app()
with tab4:
    constraints.app()
with tab5:
    limitations.app()
with tab6:
    about.app()
with tab7:
    chatbot.app()
