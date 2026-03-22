import streamlit as st
import json
from datetime import datetime

from src.embeddings import load_embedding_model
from src.pipeline import classify_ticket
from src.classifier import load_classifier


st.set_page_config(page_title="Ticket Classifier", layout="centered")

st.title("🎫 Ticket Classifier")
st.markdown("Enter an IT support ticket to classify and generate a justification.")


# ---------------------------
# 🔥 SESSION STATE
# ---------------------------
if "ticket" not in st.session_state:
    st.session_state.ticket = ""

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------
# 🧠 LOAD MODELS
# ---------------------------
@st.cache_resource
def load_models():
    embedding_model = load_embedding_model()
    clf = load_classifier()
    return embedding_model, clf


# ---------------------------
# 🔄 RESET FUNCTION
# ---------------------------
def reset_ticket():
    st.session_state.ticket = ""


# ---------------------------
# 📝 INPUT
# ---------------------------
ticket = st.text_area(
    "Ticket text",
    height=150,
    key="ticket",
    placeholder="Describe the IT issue here..."
)


# ---------------------------
# 🎛️ BUTTONS
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    classify_clicked = st.button(
        "Classify",
        disabled=not st.session_state.ticket.strip()
    )

with col2:
    st.button("🔄 New Ticket", on_click=reset_ticket)


# ---------------------------
# 🚀 CLASSIFICATION
# ---------------------------
if classify_clicked:

    with st.spinner("Processing..."):
        embedding_model, clf = load_models()
        result = classify_ticket(
            st.session_state.ticket,
            embedding_model,
            clf
        )

    st.success("Classification completed!")

    st.subheader("📌 Predicted class")
    st.write(result["class"])

    st.subheader("🧠 Justification")
    st.write(result["justification"])

    # ---------------------------
    # 📚 SAVE HISTORY
    # ---------------------------
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticket": st.session_state.ticket,
        "class": result["class"],
        "justification": result["justification"]
    }

    st.session_state.history.append(entry)


# ---------------------------
# 📜 HISTORY
# ---------------------------
if st.session_state.history:

    st.divider()
    st.subheader("📜 History")

    for i, item in enumerate(reversed(st.session_state.history), 1):
        with st.expander(f"Ticket #{i} - {item['timestamp']}"):
            st.write("**Ticket:**", item["ticket"])
            st.write("**Class:**", item["class"])
            st.write("**Justification:**", item["justification"])


# ---------------------------
# 💾 DOWNLOAD JSON
# ---------------------------
if st.session_state.history:

    st.divider()

    json_data = json.dumps(st.session_state.history, indent=2)

    st.download_button(
        label="💾 Download history as JSON",
        data=json_data,
        file_name="ticket_history.json",
        mime="application/json"
    )