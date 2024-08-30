from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

def helper_for_link_or_image(sections,text,text_type):
    split_nodes = []
    if not sections:
           split_nodes.append(TextNode(text,text_type_text))
           return split_nodes
    split_string =""
    print(text_type_text)
    for section in sections:
        split_string = text.split(f'[{section[0]}]({section[1]})') if text_type == text_type_link else text.split(f'![{section[0]}]({section[1]})')
        # if text_type == text_type_link :
        #     split_string = text.split(f'[{section[0]}]({section[1]})') 
        # else:
        #     split_string = text.split(f'![{section[0]}]({section[1]})')
        
        lstring = split_string[0]
        text = split_string[1]
        if lstring !="":
            split_nodes.append(TextNode(lstring,text_type_text))
        split_nodes.append(TextNode(section[0],text_type,section[1]))
    if text !="":
        split_nodes.append(TextNode(text,text_type_text)) 
    #split_nodes.append(TextNode(text,text_type_text))
    return split_nodes

def split_nodes_link(node):
    new_nodes = []
    for old_node in node:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        sections = extract_markdown_links(old_node.text)
        new_nodes.extend(helper_for_link_or_image(sections,old_node.text,text_type_link))
    return new_nodes

def split_nodes_image(node):
    new_nodes = []
    for old_node in node:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        sections = extract_markdown_images(old_node.text)
        new_nodes.extend(helper_for_link_or_image(sections,old_node.text,text_type_image))
    return new_nodes

