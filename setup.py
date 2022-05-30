# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Contact: ricmua (github)


from setuptools import setup
setup(
    name='md2html_links',
    version='0.1.0',
    description='A Python-Markdown extension for replacing .md file '\
               +'extensions with .html extensions in links.',
    author='ricmua',
    author_email='ricmua@whit.contact',
    url='',
    py_modules=['md2html_links'],
    install_requires = ['markdown>=3.0'],
)

