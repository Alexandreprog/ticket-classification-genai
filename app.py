import streamlit as st

from src.embeddings import load_embedding_model
from src.pipeline import classify_ticket
from src.classifier import load_classifier


st.set_page_config(page_title="Ticket Classifier", layout="centered")

st.title("🎫 Classificador de Tickets")

st.markdown("Digite um ticket de suporte de TI para classificar e gerar justificativa.")

ticket = st.text_area("Texto do ticket", height=150)


@st.cache_resource
def load_models():
    embedding_model = load_embedding_model()
    clf = load_classifier()
    return embedding_model, clf


if st.button("Classificar"):

    if not ticket.strip():
        st.warning("Digite um ticket antes de classificar.")
    else:
        with st.spinner("Processando..."):
            embedding_model, clf = load_models()
            result = classify_ticket(ticket, embedding_model, clf)

        st.success("Classificação concluída!")

        st.subheader("📌 Classe prevista")
        st.write(result["class"])

        st.subheader("🧠 Justificativa")
        st.write(result["justification"])