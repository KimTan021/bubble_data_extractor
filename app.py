import streamlit as st
import fetch_and_export
from views import documentation, constraints, limitations, about

st.set_page_config(page_title="Data Fetching and Exporting")
st.title("🚀 Bubble Data Extractor")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Fetch Data", "Documentation", "Constraints", "Limitations", "About"])

with tab1:
    fetch_and_export.app()
with tab2:
    documentation.app()
with tab3:
    constraints.app()
with tab4:
    limitations.app()
with tab5:
    about.app()