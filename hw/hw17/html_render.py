#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    INDENT = "    "

    def __init__(self, tag='', content='', **kwargs):
        self.tag = tag
        self.children = [content] if content else []
        self.attributes = kwargs

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="    "):
        string = ''
        for (key, value) in self.attributes.items():
            string += (' %s="%s"' % (key, value))

        file_out.write('%s<%s%s>\n' % (indent, self.tag, string))

        for child in self.children:
            if (type(child) == str):
                # add new content string without rendering
                file_out.write(indent + Element.INDENT + child + '\n')

            else:
                # add new child node by recursively rendering
                child.render(file_out, indent + Element.INDENT)
        file_out.write('%s</%s>\n' % (indent, self.tag))


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

    def __init__(self, content='', **kwargs):
        Element.__init__(self, 'p', content, **kwargs)


class Head(Element):

    def __init__(self):
        Element.__init__(self, 'head', '')


class OneLineTag(Element):

    def __init__(self, tag='', content='', **kwargs):
        Element.__init__(self, tag, '', **kwargs)

    def render(self, file_out, indent=''):
        file_out.write('%s%s<%s> %s </%s>\n' % (Element.INDENT, Element.INDENT,
        self.tag, self.children[0], self.tag))


class Title(OneLineTag):

    def __init__(self, content='', **kwargs):
        Element.__init__(self, 'title', content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, tag, **kwargs):
        Element.__init__(self, tag, '', **kwargs)

    def render(self, file_out, indent=''):
        string = ''
        for attribute in self.children:
            string += ('%s ' % (attribute))

        file_out.write('%s%s<%s %s/>\n' % (Element.INDENT, Element.INDENT,
        self.tag, string))


class Hr(SelfClosingTag):

    def __init__(self, content=''):
        Element.__init__(self, 'hr', content)


class Br(SelfClosingTag):

    def __init__(self, content=''):
        Element.__init__(self, 'br', content)


# class A(Element):

#     def __init__(self, link='', content='', tag='', **kwargs):
#         self.tag = tag
#         self.links = [link] if link else []
#         self.children = [content] if content else []
#         self.attributes = kwargs

#     def append(self, new_child):
#         self.children.append(new_child)

#     def render(self, file_out, indent="    "):
#         string = ''
#         for (key, value) in self.attributes.items():
#             string += (' %s="%s"' % (key, value))

#         file_out.write('%s<%s%s>\n' % (indent, self.tag, string))

#         for child in self.children:
#             if (type(child) == str):
#                 # add new content string without rendering
#                 file_out.write(indent + Element.INDENT + child + '\n')

#             else:
#                 # add new child node by recursively rendering
#                 child.render(file_out, indent + Element.INDENT)
#         file_out.write('%s</%s>\n' % (indent, self.tag))

        # A.__init__(self, link, content, 'a', **kwargs)

        # def render(self, file_out, indent=''):
        #     file_out.write('%s%s<%s%s>%s</%s>\n' % (Element.INDENT, Element.INDENT,
        #     self.tag, self.children[0], self.children[1], self.tag))


    #     file_out.write('%s%s<%s%s></%s>' % (Element.INDENT, Element.INDENT,
    #     self.tag, self.key_string, self.value_string, self.tag))
