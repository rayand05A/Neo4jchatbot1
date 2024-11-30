import streamlit as st
import traceback
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

try:
    # Tentative de configuration avec gestion explicite
    llm = ChatOpenAI(
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        model=st.secrets["OPENAI_MODEL"],
        
        # Suppression ou modification des paramètres problématiques
        openai_proxy=None,  # Explicitement aucun proxy
        # Ajoutez des paramètres supplémentaires si nécessaire
        timeout=30,  # Timeout explicite
    )

    embeddings = OpenAIEmbeddings(
        openai_api_key=st.secrets["OPENAI_API_KEY"]
    )

except Exception as e:
    st.error("Erreur de configuration du LLM")
    st.error(traceback.format_exc())
