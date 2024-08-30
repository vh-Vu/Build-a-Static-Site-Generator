import unittest
from blocks import *

class TestBlock(unittest.TestCase):
    def test_block(self):
        test = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        reference = ['# This is a heading','This is a paragraph of text. It has some **bold** and *italic* words inside of it.','* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        test_ham = markdown_to_blocks(test)
        self.assertEqual(test_ham,reference)
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), markdown_block_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), markdown_block_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), markdown_block_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), markdown_block_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), markdown_block_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), markdown_block_paragraph)



if __name__ == "__main__":
    unittest.main()