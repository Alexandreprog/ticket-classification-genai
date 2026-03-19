import streamlit as st

from src.embeddings import load_embedding_model
from src.pipeline import classify_ticket
from src.classifier import load_classifier


st.set_page_config(page_title="Ticket Classifier", layout="centered")

st.title("🎫 Ticket Classifier")

st.markdown("Enter an IT support ticket to classify and generate a justification.")

ticket = st.text_area("Ticket text", height=150)


@st.cache_resource
def load_models():
    embedding_model = load_embedding_model()
    clf = load_classifier()
    return embedding_model, clf


if st.button("Classify"):

    if not ticket.strip():
        st.warning("Enter a ticket before classifying.")
    else:
        with st.spinner("Processing..."):
            embedding_model, clf = load_models()
            result = classify_ticket(ticket, embedding_model, clf)

        st.success("Classification completed!")

        st.subheader("📌 Predicted class")
        st.write(result["class"])

        st.subheader("🧠 Justification")
        st.write(result["justification"])