import htmltext


def test_text_from_html():
    html = "<div>Привет <b>мир</b>!</div><p>Тест</p>"
    result = htmltext.text_from_html(html)
    assert result == '\nПривет мир!\nТест\n'


if __name__ == "__main__":
    test_text_from_html()
    print("Test passed.")
