import os
import re
import sys
from pathlib import Path


def parse_structure(input_file):
    input_path = Path(input_file)
    parent_dir = input_path.parent
    lines = input_path.read_text(encoding='utf-8').splitlines()

    if not lines:
        return

    # Первая строка - корневая директория
    root_line = lines[0].strip().rstrip('/')
    root_path = parent_dir / root_line
    root_path.mkdir(exist_ok=True)

    stack = [root_path]

    for line in lines[1:]:
        line = line.rstrip()
        # Парсим строку с помощью регулярного выражения
        match = re.match(r'^.*?([├└]──\s*)(.*)$', line)
        if not match:
            continue

        # Определяем отступ
        indent_part = line[: match.start(1)]
        indent = len(indent_part)

        # Считаем глубину (1 единица = 4 символа)
        depth = indent // 4 + 1

        # Получаем имя элемента
        name = match.group(2).strip()
        is_dir = name.endswith('/')
        if is_dir:
            name = name[:-1]

        # Корректируем стек директорий
        while depth < len(stack):
            stack.pop()

        # Создаём путь
        parent = stack[-1]
        full_path = parent / name

        if is_dir:
            full_path.mkdir(exist_ok=True)
            stack.append(full_path)
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.touch(exist_ok=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python create_structure.py <structure_file>')
        sys.exit(1)

    input_file = sys.argv[1]
    parse_structure(input_file)
