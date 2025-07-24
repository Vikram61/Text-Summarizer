# text_summarizer.py

# Extractive
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Abstractive
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Abstractive Setup
ab_tokenizer = T5Tokenizer.from_pretrained("t5-small")
ab_model = T5ForConditionalGeneration.from_pretrained("t5-small")

def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

def abstractive_summary(text):
    input_text = "summarize: " + text
    input_ids = ab_tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    summary_ids = ab_model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    return ab_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
