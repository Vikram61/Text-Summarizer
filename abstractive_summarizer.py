from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pretrained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

def summarize_text(text, max_input_length=512, max_output_length=150):
    # Preprocess input
    input_text = "summarize: " + text.strip().replace("\n", " ")
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=max_input_length, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_output_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


if __name__ == "__main__":
    input_text = """
    Artificial intelligence (AI) is transforming the world. From healthcare to transportation,
    AI applications are reshaping how we interact with technology. One significant area of growth is
    natural language processing, where models can understand, generate, and summarize human language
    in real-time.
    """
    summary = summarize_text(input_text)
    print("Summary:\n", summary)
