#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    INDENT = "    "

    def __init__(self, tag='', content=''):
        self.tag = tag
        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="    "):
        file_out.write('%s<%s>\n' % (indent, self.tag))
        for child in self.children:
            if (type(child) == str):
                # add new content string without rendering
                file_out.write(indent + Element.INDENT + child + '\n')

            else:
                # add new child node by recursively rendering
                child.render(file_out, indent + Element.INDENT)
        file_out.write('%s</%s>\n' % (indent, self.tag))

        #indented_content = indent + Element.INDENT + self.content
        #final_content = '<%s>\n %s \n</%s>' % (self.tag, indented_content, self.tag)
        #file_out.write(final_content)


class Html(Element):

    def __init__(self):
        Element.__init__(self, 'html', '')

    def render(self, file_out, indent=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, '')


class Body(Element):

    def __init__(self, content=''):
        Element.__init__(self, 'body', '')


class P(Element):

    def __init__(self, content=''):
        Element.__init__(self, 'p', content)

