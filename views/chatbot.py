from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import streamlit as st
from streamlit_chat import message

@st.cache_resource
def load_model():
        llm = Groq(model="llama3-70b-8192", api_key=st.secrets["API_KEY"])
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.llm = llm
        Settings.embed_model = embed_model
        documents = SimpleDirectoryReader(input_files=['README.md'], ).load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        
        return query_engine

def app():
    @st.cache_data
    def get_response_from_chatbot(user_query):
        
        query_engine = load_model()

        # Get response from the model
        response = query_engine.query(user_query)
        
        return response.response, response.source_nodes

    st.title("🤖 Hi There!")

    # Input text box for user query
    user_query = st.text_input("Ask a question:")

    if user_query:
        with st.spinner('Generating response...'):
            response, source_nodes = get_response_from_chatbot(user_query)
        # Display the user query and response in chat format
        message(user_query, is_user=True)
        message(response, is_user=False)

        st.markdown("### References:")
        for node in source_nodes:
            message(node.text, is_user=False)
