from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from converters import text_node_to_html_node


def main():
    """
    Main function to demonstrate the functionality of the Markdown parser.
    Creates sample TextNodes, converts them to HTMLNodes, and prints them.
    """
    print("Creating some TextNodes...")
    text_node = TextNode("This is regular text", TextType.TEXT)
    bold_node = TextNode("This is bold text", TextType.BOLD)
    italic_node = TextNode("This is italic text", TextType.ITALIC)
    code_node = TextNode("print('Hello, world!')", TextType.CODE)
    link_node = TextNode("Visit Boot.dev", TextType.LINK, "https://boot.dev")
    image_node = TextNode("Boot.dev Logo", TextType.IMAGE, "https://boot.dev/logo.png")
    
    print("\nConverting TextNodes to HTMLNodes...")
    text_html = text_node_to_html_node(text_node)
    bold_html = text_node_to_html_node(bold_node)
    italic_html = text_node_to_html_node(italic_node)
    code_html = text_node_to_html_node(code_node)
    link_html = text_node_to_html_node(link_node)
    image_html = text_node_to_html_node(image_node)
    
    print("\nCreating a paragraph with mixed content...")
    paragraph = ParentNode("p", [
        text_html,
        bold_html,
        text_html,
        italic_html,
        text_html,
        code_html,
        text_html,
        link_html,
        text_html,
        image_html
    ])
    
    print("\nHTML Output:")
    print(paragraph.to_html())


if __name__ == "__main__":
    main()