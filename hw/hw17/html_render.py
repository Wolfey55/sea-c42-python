#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    indent = "    "

    def __init__(self, tag='', content=''):
        self.tag = tag
        self.content = content

    def append(self, new_text):
        self.content += new_text

    def render(self, file_out, indent=""):
        indented_content = indent + self.content
        file_out.write(indented_content)


class Html(Element):

    def __init__(self):
        Element.__init__(self, 'html', '')


class Body(Element):

    def __init__(self):
        Element.__init__(self, 'body', '')


class P(Element):

    def __init__(self, content):
        Element.__init__(self, 'p', content)
