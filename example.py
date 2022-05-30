

from markdown import markdown
from md2html_links import CustomLinkExtension

data = 'Some text and a [link](path/to/a/document.md).\n'
html = markdown(data, extensions=[CustomLinkExtension()])
print(f'ORIGINAL:\n{data}\n\nCONVERTED:\n{html}')


