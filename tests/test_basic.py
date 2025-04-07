import htmltext

def test_text_from_html():
    html = "<div>Привет <b>мир</b>!</div><p>Тест</p>"
    result = htmltext.text_from_html(html)
    assert result == "Привет мир!\nТест"
