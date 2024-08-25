from textnode import TextNode

def main():
    new_textnode = TextNode('This is a text node','bold','https://www.boot.dev')
    print(new_textnode.__repr__())


if __name__ == "__main__":
    main()