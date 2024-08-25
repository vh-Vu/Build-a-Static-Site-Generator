from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('No Tag')
        elif not self.children:
            raise ValueError('No childrens')
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.create_tag()}</{self.tag}>"

    def create_tag(self):
        text =""
        for child in self.children:
            if isinstance(child,ParentNode):
                text+=child.to_html()
            elif isinstance(child,LeafNode):
                text+=child.create_tag()
        return text



