

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result =""
        for key,value in self.props.items():
            result+= f' {key}="{value}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('No Tag')
        elif not self.children:
            raise ValueError('No childrens')
        else:
            child_html = ""
            for child in self.children:
                child_html+=child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

    def create_tag(self):
        text =""
        for child in self.children:
            if isinstance(child,ParentNode):
                text+=child.to_html()
            elif isinstance(child,LeafNode):
                text+=child.create_tag()
        return text

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        return self.create_tag()

    def create_tag(self):
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
