from io import StringIO

import markdown
from markdown.inlinepatterns import LINK_RE
from markdown.test_tools import TestCase
from md2html_links import CustomLinkExtension

class ProcessorTest(TestCase):
    default_kwargs = {'extensions': [CustomLinkExtension()]}

    def test_relative(self):
        self.assertMarkdownRenders(
            'hi [linkme](./somedir/index.md)',
            '<p>hi <a href="./somedir/index.html">linkme</a></p>'
        )
        self.assertMarkdownRenders(
            'hi [linkme](../somedir/index.md)',
            '<p>hi <a href="../somedir/index.html">linkme</a></p>'
        )
        
    def test_absolute(self):
        self.assertMarkdownRenders(
            'hi [linkme](/somedir/index.md)',
            '<p>hi <a href="/somedir/index.html">linkme</a></p>'
        )
        
    def test_fully_qualified(self):
        self.assertMarkdownRenders(
            'hi [linkme](http://www.example.com/somedir/index.md)',
            '<p>hi <a href="http://www.example.com/somedir/index.md">linkme</a></p>'
        )
        self.assertMarkdownRenders(
            'hi [linkme](https://www.example.com/somedir/index.md)',
            '<p>hi <a href="https://www.example.com/somedir/index.md">linkme</a></p>'
        )


