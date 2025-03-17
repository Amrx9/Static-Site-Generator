class HTMLNode:
    """
    Base class representing an HTML node.
    This is an abstract class that should be extended by specific node types.
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initialize an HTMLNode.
        
        Args:
            tag (str, optional): The HTML tag name (e.g., "p", "a", "h1")
            value (str, optional): The text content of the node
            children (list, optional): List of child HTMLNode objects
            props (dict, optional): HTML attributes as key-value pairs
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Convert the node to HTML. This is an abstract method.
        
        Raises:
            NotImplementedError: This method should be implemented by subclasses
        """
        raise NotImplementedError

    def props_to_html(self):
        """
        Convert HTML properties to a string.
        
        Returns:
            str: HTML attributes string with leading spaces (e.g., ' href="url" class="btn"')
        """
        if self.props is None:
            return ""
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string

    def __repr__(self):
        """
        Return a string representation of the HTMLNode.
        
        Returns:
            str: String representation showing all properties
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """
    A leaf node in the HTML tree - represents a node with no children,
    just a tag and value.
    """
    def __init__(self, tag, value, props=None):
        """
        Initialize a LeafNode.
        
        Args:
            tag (str): The HTML tag name (can be None for raw text)
            value (str): The text content of the node
            props (dict, optional): HTML attributes as key-value pairs
        """
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Convert the leaf node to HTML.
        
        Returns:
            str: HTML string representation
            
        Raises:
            ValueError: If the value is None
        """
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """
    A parent node in the HTML tree - represents a node with children.
    """
    def __init__(self, tag, children, props=None):
        """
        Initialize a ParentNode.
        
        Args:
            tag (str): The HTML tag name
            children (list): List of child HTMLNode objects
            props (dict, optional): HTML attributes as key-value pairs
        """
        super().__init__(tag, None, children, props)

    def to_html(self):
        """
        Convert the parent node and all its children to HTML.
        
        Returns:
            str: HTML string representation
            
        Raises:
            ValueError: If tag or children are None
        """
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError("All parent nodes must have children.")
        
        html = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html