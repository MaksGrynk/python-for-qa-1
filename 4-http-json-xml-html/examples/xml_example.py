
import xml.etree.ElementTree as etree


def main():
    # parse xml
    tree = etree.parse('feed.xml')

    # get root object
    root = tree.getroot() # <Element 'rss' at 0x102f02910>

    # Elements Are Lists

    # Attributes Are Dictonaries

    # findall()

    # find()


if __name__ == '__main__':
    main()
