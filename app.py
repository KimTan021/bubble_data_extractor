import streamlit as st
import fetch_and_export
from views import users_guide, developers_guide, constraints, limitations, about

st.set_page_config(page_title="Bubble Data Extractor", page_icon="🚀")
st.title("🚀 Bubble Data Extractor")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Fetch Data", "Users Guide", "Developers Guide", "Constraints", "Limitations", "About"])

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