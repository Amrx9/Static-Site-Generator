import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    """
    Test cases for the TextNode class.
    Tests equality comparisons between TextNode instances with various properties.
    """
    
    def test_eq(self):
        """Test that two TextNodes with identical properties are equal."""
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)

    def test_different_text(self):
        """Test that TextNodes with different text content are not equal."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_type(self):
        """Test that TextNodes with different text types are not equal."""
        node = TextNode("This is for test", TextType.TEXT)
        node2 = TextNode("This is for test", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        """Test that TextNodes with default None URLs are equal if other properties match."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)
        self.assertEqual(node, node2)

    def test_different_url(self):
        """Test that TextNodes with different URLs are not equal."""
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_url_vs_none(self):
        """Test that TextNodes with URL vs None URL are not equal."""
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()