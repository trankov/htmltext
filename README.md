# htmltext

Быстрый и минималистичный Python-модуль на C для извлечения текста из HTML.

## Пример

```python
import htmltext
text = htmltext.text_from_html("<p>Привет <b>мир</b>!</p>")
print(text)
# Привет мир!
