# 🎫 Ticket Classification with Generative AI

## 📌 Overview

This project implements a ticket classification system using machine learning and generative AI techniques. It combines traditional ML models with embeddings and LLM-based justification to classify support tickets efficiently.

The application is served through a Streamlit interface, allowing interactive classification of tickets.

---

## 🗂️ Project Structure

```
ticket-classification-genai/
│
├── app.py                  # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (API keys)
│
├── data/                  # Dataset
│   └── tickets.csv
│
├── docs/                  # Sphinx documentation
│   ├── build/             # Generated documentation (HTML and PDF)
│   ├── source/            # Sphinx source files
│   ├── make.bat
│   └── Makefile
│
├── models/                # Trained models
│   └── classifier.joblib
│
├── notebooks/             # Experiments and model training
│   └── experiment.ipynb
│
├── src/                   # Core source code
│   ├── __init__.py
│   ├── classifier.py      # Model training and prediction logic
│   ├── data_prep.py       # Data preprocessing
│   ├── embeddings.py      # Text embeddings generation
│   ├── justification.py   # LLM-based justification (Groq)
│   ├── metrics.py         # Evaluation metrics
│   └── pipeline.py        # End-to-end pipeline
```

---

## 📚 Documentation

The project documentation was generated using **Sphinx**.

You can access it in three ways:

* 📄 **Inline in the code**: Detailed docstrings inside functions and modules
* 🌐 **Web version**: Open the file below in your browser:

  ```
  docs/build/html/index.html
  ```
* 📑 **PDF version**:
  👉 [Download Documentation PDF](docs/build/pdf/TicketClassificationDoc.pdf)

---

## 🧪 Experiments

The notebook below is used for experimentation, testing, and model training:

```
notebooks/experiment.ipynb
```

---

## ⚙️ Requirements

All required libraries are listed in:

```
requirements.txt
```

To install them, run:

```bash
pip install -r requirements.txt
```

---

## 🔐 API Configuration

This project uses the **Groq API** for LLM-based processing.

Before running the project, you must configure your API key.

Create a `.env` file (if not already present) and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ How to Run the Project

After installing dependencies and configuring the API key, run:

```bash
streamlit run app.py
```

This will start the Streamlit application in your browser.

---

## 🚀 Features

* Ticket classification using machine learning
* Embedding-based text representation
* LLM-powered justification (via Groq)
* Interactive UI with Streamlit
* Modular and well-documented architecture

---

## 🧠 Notes

* The `src/` folder contains the full ML pipeline and logic
* The `notebooks/` folder is intended for experimentation only
* The `docs/` folder contains auto-generated documentation via Sphinx
* The `models/` folder contains trained models
