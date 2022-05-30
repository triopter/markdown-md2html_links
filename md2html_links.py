""" A Python-Markdown extension for replacing .md file extensions with .html 
    extensions in links.

"""

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Contact: ricmua (github)


# Imports.
import os
from markdown import Extension
from markdown.inlinepatterns import LinkInlineProcessor
from markdown.inlinepatterns import LINK_RE



# Inline processor.
class CustomLinkInlineProcessor(LinkInlineProcessor):
    
    def getLink(self, *args, **kwargs):
        
        # Invoke the superclass method / default link processor.
        (href, title, index, handled) = super().getLink(*args, **kwargs)
        
        # Split the extension and replace it if it is .md.
        parts = os.path.splitext(href)
        ext = '.html' if (parts[1] == '.md') else parts[1]
        href = ''.join((parts[0], ext))
        
        # Return the result.
        return (href, title, index, handled)
    
  

# Extension.
class CustomLinkExtension(Extension):
    
    def extendMarkdown(self, md):
        
        # Hard-code the default link processor priority.
        # https://github.com/Python-Markdown/markdown/blob
        # /a767b2daaad78ba32d45a4f1dabb7c5e218f030a/markdown
        # /inlinepatterns.py#L79
        # This is approach is overridden, in favor of dynamically retrieving 
        # the priority (see below).
        priority = 160
        
        # Set the priority of the link processor.
        # The mechanism for retrieving the priority is not documented.
        # So there is some risk that this will break with future 
        # Python-Markdown updates.
        priority_map = {p.name: p.priority for p in md.inlinePatterns._priority}
        priority = priority_map['link']
        
        # De-register the default link processor.
        md.inlinePatterns.deregister('link')
        
        # Replace the default link processor with the extension.
        pattern = CustomLinkInlineProcessor(LINK_RE, md)
        md.inlinePatterns.register(pattern, 'link', priority)

