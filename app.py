import streamlit as st
from text_summarizer import extractive_summary, abstractive_summary
import PyPDF2
import io

st.set_page_config(page_title="Text Summarizer", layout="wide")
st.title("📝 Text Summarizer")

uploaded_file = st.file_uploader("Upload a PDF (optional)", type=["pdf"])
text = ""

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    st.success("✅ PDF text extracted successfully!")

# Allow manual text entry
manual_text = st.text_area("Or enter text manually", height=300)
if manual_text.strip():
    text = manual_text  # Override PDF text if user enters manually

mode = st.radio("Choose summarization type", ("Extractive", "Abstractive"))

if mode == "Extractive":
    num_sentences = st.slider("Number of sentences in summary", min_value=1, max_value=10, value=3)

    if st.button("Generate Extractive Summary"):
        if text.strip():
            summary = extractive_summary(text, num_sentences)
            st.subheader("📄 Extractive Summary")
            st.write(summary)
        else:
            st.warning("Please upload a PDF or enter some text!")

else:
    min_len = st.slider("Minimum summary length (words)", 10, 150, 30)
    max_len = st.slider("Maximum summary length (words)", min_len + 10, 300, 100)

    if st.button("Generate Abstractive Summary"):
        if text.strip():
            summary = abstractive_summary(text, min_len, max_len)
            st.subheader("📄 Abstractive Summary")
            st.write(summary)
        else:
            st.warning("Please upload a PDF or enter some text!")
