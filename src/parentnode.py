from src.htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError("All parent nodes must have children.")
        
        props_html = ""
        if self.props:
            for prop, value in self.props.items():
                props_html += f' {prop}="{value}"'
        
        html = f"<{self.tag}{props_html}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html