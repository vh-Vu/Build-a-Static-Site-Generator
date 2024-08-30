import re
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

def markdown_to_html_node(markdown):
    
