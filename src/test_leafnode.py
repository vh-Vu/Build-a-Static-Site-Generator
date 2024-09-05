import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node1_ref  = '<p>This is a paragraph of text.</p>'
        node2_ref = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node1.to_html(),node1_ref)
        self.assertEqual(node2.to_html(),node2_ref)


if __name__ == "__main__":
    unittest.main()