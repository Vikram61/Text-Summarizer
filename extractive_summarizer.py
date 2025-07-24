from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def extractive_summary(text,sentence_count=3):

    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document,sentence_count)

    return ''.join(str(sentence) for sentence in summary)










# Test run
if __name__ == "__main__":
    sample_text = """
    Natural Language Processing (NLP) is a field of artificial intelligence 
    that focuses on the interaction between humans and computers through natural language. 
    The ultimate objective of NLP is to read, decipher, understand, and make sense of 
    human language in a valuable way. NLP is used in various applications like 
    sentiment analysis, machine translation, chatbot development, and summarization.
    """
    print("Extractive Summary:\n", extractive_summary(sample_text, sentence_count=2))