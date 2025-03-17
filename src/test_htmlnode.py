import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from converters import text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    """Test cases for HTMLNode, LeafNode, ParentNode, and converter functions."""
    
    # Your existing test methods remain the same
    # Only the imports at the top need to change
    
    # ... rest of the test code ...


if __name__ == "__main__":
    unittest.main()