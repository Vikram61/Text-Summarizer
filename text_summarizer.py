# text_summarizer.py
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from transformers import pipeline

# Load HuggingFace summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer_lsa = LsaSummarizer()
    summary = summarizer_lsa(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

def abstractive_summary(text, min_len=30, max_len=100):
    summary = summarizer(text, min_length=min_len, max_length=max_len)[0]['summary_text']
    return summary
