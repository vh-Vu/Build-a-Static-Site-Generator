import re
from split_nodes_delimiter import text_to_textnodes
from htmlnode import *
from textnode import *
markdown_block_paragraph = "paragraph"
markdown_block_heading = "heading"
markdown_block_code = "code"
markdown_block_quote = "quote"
markdown_block_unordered_list = "unordered_list"
markdown_block_ordered_list= "ordered_list"

def markdown_to_blocks(markdown):
    result = []
    string = ""
    for line in markdown.split('\n'):
        l = line.strip()
        if l: 
            string +=l+'\n'
        else:
            if string:
                result.append(string[:-1])
                string = ""
    if string:
        result.append(string[:-1])
    return result

def isHeading(line):
    match = re.findall(r'\#{1,6} ',line)
    return True if match else False

def is_code_block(line):
    match = re.findall(r'\`\`\`(.*?)\`\`\`',line,re.DOTALL)
    return True if match else False

def is_block_quotes(line):
    match = re.findall(r'\>(.*?)',line)
    return True if match else False

def is_ordered_list(line):
    match = re.findall(r'\d+.+ +(.*?)',line)
    return True if match else False

def is_unordered_list(line):
    match = re.findall(r'^[*-] +(.*)',line)
    return True if match else False


def block_to_block_type(block):
    if isHeading(block):
        return markdown_block_heading
    elif is_code_block(block):
        return markdown_block_code
    elif is_block_quotes(block):
        return markdown_block_quote
    elif is_ordered_list(block):
        return markdown_block_ordered_list
    elif is_unordered_list(block):
        return markdown_block_unordered_list
    else:
        return markdown_block_paragraph


def get_heading(x):
    if x.startswith('###### '):
        return 6
    elif x.startswith('##### '):
        return 5
    elif x.startswith('#### '):
        return 4
    elif x.startswith('### '):
        return 3
    elif x.startswith('## '):
        return 2
    elif x.startswith('# '):
        return 1
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    content = []
    for block in blocks:
        content.append(handing_block(block_to_block_type(block),block))
    return ParentNode('div',content)




def excute():
    def helper(text):
        child = []
        inline = text_to_textnodes(text)
        for ch in inline:
            child.append(text_node_to_html_node(ch))
        return child
    return helper

def helper_for_list(block,isOrder):
    li = []
    replace = r'^\d+\.\s' if isOrder else r'^[*-]\s'
    for line in block.split('\n'):
        li.append(ParentNode('li',excute()(re.sub(replace,'',line ))))
    return li


def handing_block(block_type, content):
    if block_type ==  markdown_block_heading:
        return ParentNode(f'h{get_heading(content)}',excute()(content.lstrip('# ')))
    elif block_type == markdown_block_code:
        text = content.strip('```')
        return ParentNode('pre',[LeafNode('code',content.lstrip('```').strip())])
    elif block_type == markdown_block_quote:
        block_quote_list = []
        for line in content.split('\n'):
            block_quote_list.append(line.lstrip('>').strip())
        return ParentNode('blockquote',excute()(' '.join(block_quote_list)))
    elif block_type == markdown_block_unordered_list:
        return ParentNode('ul',helper_for_list(content,False))
    elif block_type == markdown_block_ordered_list:
        return ParentNode('ol',helper_for_list(content,True))
    elif block_type == markdown_block_paragraph:
        paragraph = []
        for line in content.split('\n'):
            paragraph.append(line.strip())
        return ParentNode('p',excute()(' '.join(paragraph)))






