from pathlib import Path

from setuptools import Extension, setup


module = Extension('htmltext', sources=['htmltext.c'])

setup(
    name='htmltext',
    version='0.1',
    description='Fast UTF-8-safe HTML to text converter',
    author='Aleksei Trankov',
    author_email='shoyna@ognzm.ru',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    ext_modules=[module],
    python_requires='>=3.8',
)
