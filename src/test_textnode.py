import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "italic")
        node4 = TextNode("This is a text node", "italic")
        node6 = TextNode("This is a text node", "italic","https://www.boot.dev")
        node5 = TextNode("This is a text node", "italic","https://www.boot.dev")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5,node6)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag,None)
        self.assertEqual(htmlnode.value,"This is a text node")

    def test_image(self):
        node = TextNode("This is a text node", text_type_image,"https://www.boot.dev")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag,"img")
        self.assertEqual(htmlnode.value,"")
        self.assertEqual(htmlnode.props,{"src":"https://www.boot.dev","alt":"This is a text node"})

    def test_bold(self):
        node = TextNode("This is a text node", text_type_bold)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag,"b")
        self.assertEqual(htmlnode.value,"This is a text node")

if __name__ == "__main__":
    unittest.main()