from enum import Enum


class TextType(Enum):
    """
    Enum representing the different types of inline text elements
    that can be parsed from Markdown.
    """
    TEXT = "text"     # Regular text
    BOLD = "bold"     # Bold text (**text**)
    ITALIC = "italic" # Italic text (_text_)
    CODE = "code"     # Code text (`text`)
    LINK = "link"     # Link text ([text](url))
    IMAGE = "image"   # Image text (![alt](url))


class TextNode:
    """
    Class representing a node of text with a specific type.
    TextNodes are the intermediate representation between Markdown and HTML.
    """
    def __init__(self, text, text_type, url=None):
        """
        Initialize a TextNode.
        
        Args:
            text (str): The text content of the node
            text_type (TextType): The type of text this node contains
            url (str, optional): The URL for links or images, defaults to None
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Check if two TextNode objects are equal.
        
        Args:
            other: The object to compare with
            
        Returns:
            bool: True if all properties are equal, False otherwise
        """
        if isinstance(other, TextNode):
            return (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
        return False

    def __repr__(self):
        """
        Return a string representation of the TextNode.
        
        Returns:
            str: String representation in the format TextNode(text, text_type, url)
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"