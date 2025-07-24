import streamlit as st
from text_summarizer import extractive_summary, abstractive_summary
import PyPDF2

st.set_page_config(page_title="Text Summarizer App", layout="centered")
st.title("📝 Text Summarizer (Extractive + Abstractive)")

# --- Text Input Method ---
input_method = st.radio("Choose Input Method:", ["Type/Paste Text", "Upload File"])

text = ""

if input_method == "Type/Paste Text":
    text = st.text_area("Enter the text to summarize", height=300)

else:
    uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
    
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

# --- Summarization Method ---
method = st.radio("Choose summarization type:", ["Extractive", "Abstractive"])

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please provide input text.")
    else:
        with st.spinner("Summarizing..."):
            if method == "Extractive":
                summary = extractive_summary(text)
            else:
                summary = abstractive_summary(text)
        st.subheader("Summary")
        st.success(summary)
