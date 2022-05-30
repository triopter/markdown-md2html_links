
This is a [Python-Markdown](https://python-markdown.github.io/) extension for replacing .md file extensions with .html extensions in links. This is especially useful for maintaining Markdown collections file that contain relative internal links, but are still parser-agnostic. There is a related [GitHub issue](https://github.com/Python-Markdown/markdown/issues/1094).

## Installation

The package must be available in the Python path. A [setup.py](https://docs.python.org/3/distutils/setupscript.html#setup-script) script is included.

## Usage

Example:

```python
from markdown import markdown
from md2html_links import CustomLinkExtension

data = 'Some text and a [link](path/to/a/document.md).\n'
html = markdown(data, extensions=[CustomLinkExtension()])
print(f'ORIGINAL:\n{data}\n\nCONVERTED:\n{html}')
```

The output is as follows:

```
ORIGINAL:
Some text and a [link](path/to/a/document.md).


CONVERTED:
<p>Some text and a <a href="path/to/a/document.html">link</a>.</p>
```

## Development notes

This extension has been created following the guidance of the Python-Markdown [extensions tutorial](https://github.com/Python-Markdown/markdown/wiki/Tutorial-1---Writing-Extensions-for-Python-Markdown) and the [extensions API documentation](https://python-markdown.github.io/extensions/api).

The approach is to replace the [LinkInlineProcessor](https://github.com/Python-Markdown/markdown/blob/a767b2daaad78ba32d45a4f1dabb7c5e218f030a/markdown/inlinepatterns.py#L590) [inline processor](https://python-markdown.github.io/extensions/api/#inlineprocessors) with a slightly modified version of the same. It is given the same priority as the original in the Python-Markdown [registry](https://python-markdown.github.io/extensions/api/#registries).

An alternative approach was also [suggested](https://github.com/Python-Markdown/markdown/issues/1094#issuecomment-1140189488) by [@venthur](https://github.com/venthur).

