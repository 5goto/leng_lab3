from transformers import pipeline


# Загрузка предобученной модели BERT для реферирования текста
summarizer = pipeline("summarization")

# Пример текста для реферирования

with open('./example.txt', 'r') as example_file:
    text = example_file.read()

# Реферирование текста
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    print(summary[0]['summary_text'])