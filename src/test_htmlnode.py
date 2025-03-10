import unittest

from htmlnode import *
from leafnode import *


class TestHTMLNode(unittest.TestCase):
    def test_init_values(self):
        html_node = HTMLNode("p", "i am a text inside a paragraph", None, None)
        self.assertEqual(html_node.tag, "p")
        self.assertEqual(html_node.value, "i am a text inside a paragraph")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_children(self):
        child_node = HTMLNode("li", "Item 1", None, None)
        parent_node = HTMLNode("ul", None, [child_node], None)
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0], child_node)

    def test_multiple_children(self):
        child1 = HTMLNode("li", "Item 1", None, None)
        child2 = HTMLNode("li", "Item 2", None, None)
        parent = HTMLNode("ul", None, [child1, child2], None)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0], child1)
        self.assertEqual(parent.children[1], child2)

    def test_empty_props(self):
        node = HTMLNode("div", "content", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_none_props(self):
        node = HTMLNode("span", "text", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props(self):
        prop = {
            "href": "https://google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "Website", None, prop)
        self.assertEqual(node.props, prop)
        self.assertEqual(
            node.props_to_html(), ' href="https://google.com" target="_blank"'
        )
        print(node.props_to_html())

    def test_props_with_special_chars(self):
        props = {"data-test": 'value"with"quotes', "class": "my-class"}
        node = HTMLNode("div", "content", None, props)
        self.assertEqual(
            node.props_to_html(), ' data-test="value"with"quotes" class="my-class"'
        )

    def test_repr(self):
        node = HTMLNode("p", "text", None, {"class": "bold"})
        self.assertIn("HTMLNode", repr(node))
        self.assertIn("p", repr(node))
        self.assertIn("text", repr(node))
        self.assertIn("bold", repr(node))

    # unit test for leafnode.py
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_attributes(self):
        node = LeafNode(
            "a", "Click me!", {"href": "https://boot.dev", "class": "button"}
        )
        self.assertIn('href="https://boot.dev"', node.to_html())
        self.assertIn('class="button"', node.to_html())
        self.assertIn(">Click me!</a>", node.to_html())

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src": "image.jpg", "alt": "An image"})
        html = node.to_html()
        self.assertIn('src="image.jpg"', html)
        self.assertIn('alt="An image"', html)
        self.assertIn("<img", html)
        self.assertIn("></img>", html)


if __name__ == "__main__":
    unittest.main()
