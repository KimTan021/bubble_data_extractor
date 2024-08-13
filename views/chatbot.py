from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import streamlit as st
from streamlit_chat import message

def app():
    def get_response_from_chatbot(user_query):
        llm = Groq(model="llama3-70b-8192", api_key=st.secrets["API_KEY"])
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.llm = llm
        Settings.embed_model = embed_model
        documents = SimpleDirectoryReader(input_files=['README.md'], ).load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()

        # Get response from the model
        response = query_engine.query(user_query)
        
        return response.response, response.source_nodes

    # Streamlit app
    st.title("Bubble Chatbot 🤖")

    # Input text box for user query
    user_query = st.text_input("Ask a question:")

    if user_query:

        response, source_nodes = get_response_from_chatbot(user_query)
        # Display the user query and response in chat format
        message(user_query, is_user=True)
        message(response, is_user=False)

        st.markdown("### References:")
        for node in source_nodes:
            message(node.text, is_user=False)
