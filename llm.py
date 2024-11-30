import streamlit as st
import traceback
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Tentative de configuration avec gestion explicite
try:
    llm = ChatOpenAI(
        openai_api_key=st.secrets["OPENAI_API_KEY"],  # Utilisation de la clé API stockée dans les secrets de Streamlit
        model=st.secrets["OPENAI_MODEL"],  # Modèle OpenAI à utiliser
        timeout=30  # Timeout explicite pour les appels API
    )

    embeddings = OpenAIEmbeddings(
        openai_api_key=st.secrets["OPENAI_API_KEY"]  # Utilisation de la même clé API pour les embeddings
    )

except Exception as e:
    st.error(f"Erreur lors de la configuration de l'OpenAI API: {str(e)}")
    traceback.print_exc()

# Déclaration explicite des éléments à exposer si nécessaire
__all__ = ['llm']
