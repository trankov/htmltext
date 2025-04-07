#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_INPUT_SIZE (5 * 1024 * 1024)  // 5 MB

// Быстрая проверка на блочные HTML-теги
static int is_block_tag(const char *tag, size_t len) {
    // Предварительно вычисленные длины тегов для избежания вызова strlen
    static const char *block_tags[] = {
        "div", "p", "br", "section", "article", "header", "footer",
        "ul", "ol", "li", "table", "tr", "td",
        "h1", "h2", "h3", "h4", "h5", "h6"
    };
    static const size_t tag_lengths[] = {
        3, 1, 2, 7, 7, 6, 6,
        2, 2, 2, 5, 2, 2,
        2, 2, 2, 2, 2, 2
    };
    static const size_t num_tags = sizeof(block_tags) / sizeof(block_tags[0]);

    for (size_t i = 0; i < num_tags; i++) {
        if (tag_lengths[i] == len && strncasecmp(tag, block_tags[i], len) == 0)
            return 1;
    }
    return 0;
}

static PyObject* text_from_html(PyObject *self, PyObject *args) {
    PyObject *input_unicode;

    if (!PyArg_ParseTuple(args, "U", &input_unicode)) {
        return NULL;
    }

    Py_ssize_t len = 0;
    const char *html = PyUnicode_AsUTF8AndSize(input_unicode, &len);
    if (!html || len > MAX_INPUT_SIZE) {
        PyErr_SetString(PyExc_ValueError, "Input too large or invalid UTF-8");
        return NULL;
    }

    // Выделяем память с запасом для возможных '\n', но не более чем 2*len
    // Используем malloc вместо calloc для ускорения, т.к. мы заполняем все байты вручную
    char *out = malloc(len * 2 + 1);  // +1 для завершающего нуля
    if (!out) return PyErr_NoMemory();

    size_t out_len = 0;
    Py_ssize_t i = 0;

    // Флаги для отслеживания, находимся ли мы внутри тегов, содержимое которых нужно удалить
    int in_script = 0;
    int in_svg = 0;

    while (i < len) {
        if (html[i] == '<') {
            i++;  // skip '<'
            // Py_ssize_t tag_start = i;

            // Skip possible /
            int is_closing = 0;
            if (i < len && html[i] == '/') {
                i++;
                is_closing = 1;
            }
            Py_ssize_t name_start = i;

            while (i < len && ((html[i] >= 'a' && html[i] <= 'z') || (html[i] >= 'A' && html[i] <= 'Z'))) {
                i++;
            }

            size_t tag_len = i - name_start;

            // Проверка на теги, содержимое которых нужно удалить
            // Оптимизированная проверка с использованием первого символа для быстрого отсеивания
            if (tag_len > 0) {
                char first_char = html[name_start] | 32; // Преобразуем в нижний регистр

                if (first_char == 's') {
                    if (tag_len == 6 && strncasecmp(&html[name_start], "script", 6) == 0) {
                        in_script = !is_closing;
                    } else if (tag_len == 3 && strncasecmp(&html[name_start], "svg", 3) == 0) {
                        in_svg = !is_closing;
                    }
                }
            }

            int block_tag = is_block_tag(&html[name_start], tag_len);

            // Skip until '>' с защитой от бесконечного цикла
            Py_ssize_t safety_counter = 0;
            const Py_ssize_t max_tag_len = 1000; // разумное ограничение на длину тега
            while (i < len && html[i] != '>' && safety_counter < max_tag_len) {
                i++;
                safety_counter++;
            }
            if (i < len) i++;

            if (block_tag && (out_len == 0 || out[out_len - 1] != '\n')) {
                out[out_len++] = '\n';
            }
            continue;
        }

        // Пропускаем содержимое тегов script и svg
        if (in_script || in_svg) {
            i++;
            continue;
        }

        if (html[i] == '&') {
            // Skip until ';' с защитой от бесконечного цикла
            Py_ssize_t safety_counter = 0;
            const Py_ssize_t max_entity_len = 10; // разумное ограничение на длину HTML-сущности
            while (i < len && html[i] != ';' && safety_counter < max_entity_len) {
                i++;
                safety_counter++;
            }
            if (i < len) i++;
            continue;
        }

        // Copy UTF-8 sequence (multi-byte safe)
        unsigned char c = html[i];
        if (c < 0x80) {
            // ASCII
            if (c == '\r') {
                i++;
                continue;
            }
            if (c == '\n') {
                // Оптимизированный подсчет количества последовательных переносов строк
                // Быстрая проверка на наличие второго переноса строки
                int has_multiple_newlines = 0;
                Py_ssize_t temp_i = i + 1;

                // Проверяем только наличие второго переноса, а не считаем все
                while (temp_i < len && (html[temp_i] == '\n' || html[temp_i] == '\r')) {
                    if (html[temp_i] == '\n') {
                        has_multiple_newlines = 1;
                        break;
                    }
                    temp_i++;
                }

                // Добавляем один или два переноса строки в зависимости от количества
                if (has_multiple_newlines) {
                    // Добавляем максимум два переноса строки
                    if (out_len == 0) {
                        // Пустой выходной буфер
                        out[out_len++] = '\n';
                        out[out_len++] = '\n';
                    } else if (out[out_len - 1] != '\n') {
                        // Нет переноса в конце
                        out[out_len++] = '\n';
                        out[out_len++] = '\n';
                    } else if (out_len == 1 || out[out_len - 2] != '\n') {
                        // Есть один перенос в конце
                        out[out_len++] = '\n';
                    }
                    // Иначе уже есть два переноса, ничего не делаем
                } else {
                    // Один перенос строки оставляем как есть
                    if (out_len == 0 || out[out_len - 1] != '\n') {
                        out[out_len++] = '\n';
                    }
                }

                // Пропускаем все переносы строк
                while (i < len && (html[i] == '\n' || html[i] == '\r')) i++;
                continue;
            }
            // Пропускаем пробелы в начале текста
            if (c == ' ' && (out_len == 0 || out[out_len - 1] == '\n')) {
                i++;
                continue;
            }

            // Не добавляем пробел, если следующий символ - перенос строки
            if (c == ' ' && i + 1 < len && (html[i + 1] == '\n' || html[i + 1] == '\r')) {
                i++;
                continue;
            }

            out[out_len++] = c;
            i++; // Увеличиваем индекс после обработки ASCII-символа
        } else {
            // Многобайтовые UTF-8 последовательности
            // Оптимизированное определение длины UTF-8 последовательности
            int bytes;
            if ((c & 0x80) == 0) { // Это не должно произойти, но для надежности
                bytes = 1;
            } else if ((c & 0xE0) == 0xC0) { // 110xxxxx - 2 байта
                bytes = 2;
            } else if ((c & 0xF0) == 0xE0) { // 1110xxxx - 3 байта
                bytes = 3;
            } else {
                bytes = 4; // 11110xxx - 4 байта или некорректная последовательность
            }

            for (int j = 0; j < bytes && i < len; j++) {
                out[out_len++] = html[i++];
            }
        }
    }

    // Удалить лишние пробелы в конце
    while (out_len > 0 && out[out_len - 1] == ' ') {
        out_len--;
    }

    // Ограничиваем количество переносов строк в конце до двух
    if (out_len >= 2 && out[out_len - 1] == '\n' && out[out_len - 2] == '\n') {
        // Уже есть два переноса, удаляем все дополнительные
        while (out_len > 2 && out[out_len - 3] == '\n') {
            out_len--;
        }
    } else if (out_len >= 1 && out[out_len - 1] == '\n') {
        // Есть один перенос, оставляем его
    } else {
        // Нет переносов в конце, это нормально
    }

    // Добавляем завершающий нуль для безопасности
    out[out_len] = '\0';

    PyObject *result = PyUnicode_DecodeUTF8(out, out_len, "strict");
    free(out);

    // Проверка на ошибки декодирования
    if (result == NULL) {
        PyErr_SetString(PyExc_UnicodeDecodeError, "Failed to decode extracted text as UTF-8");
        return NULL;
    }

    return result;
}

static PyMethodDef HtmlTextMethods[] = {
    {"text_from_html", text_from_html, METH_VARARGS, "Extract plain text from HTML (UTF-8 safe)"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef htmltextmodule = {
    PyModuleDef_HEAD_INIT,
    "htmltext",
    NULL,
    -1,
    HtmlTextMethods
};

PyMODINIT_FUNC PyInit_htmltext(void) {
    return PyModule_Create(&htmltextmodule);
}
