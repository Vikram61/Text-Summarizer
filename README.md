# 📝 Text Summarizer App

An AI-powered web application that provides **Extractive** and **Abstractive** summarization for text and PDF documents. Built using **Streamlit**, **HuggingFace Transformers**, and traditional NLP techniques.

## 🚀 Features

- 🔍 **Extractive Summarization**: Selects the most important sentences from the original text.
- 🧠 **Abstractive Summarization**: Generates a human-like summary by paraphrasing the content.
- 📄 **PDF Support**: Upload and summarize text directly from PDF files.
- 📏 Adjustable summary length:
  - Number of sentences for extractive
  - Word range for abstractive
- ⚡ Lightweight and fast with a clean UI
- 📦 Easily deployable as a Streamlit app

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit
- **Abstractive Model**: `t5-small` via HuggingFace Transformers
- **Extractive Model**: Sumy (LexRank algorithm)
- **PDF Parsing**: PyPDF2
- **Tokenizer**: SentencePiece

## 🧪 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
