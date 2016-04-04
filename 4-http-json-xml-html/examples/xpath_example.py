
import xml.etree.ElementTree as etree


def main():
    course_xml = etree.parse('course.xml')
    root = course_xml.getroot()

    # find all examples
    print(root.findall('.//example'))

    # returns all modules
    print(root.findall('./modules/*'))

    # returns first example in module 5
    print(root.findall('.//module[@id="module5"]//example[0]'))

    # returns modules that have examples
    print(root.findall('.//examples/..'))
    print(root.findall('.//module[examples]'))

    # returns modules that have id attribute
    print(root.findall('.//module[@id]'))

    print(root.findall('.//module//[example="Parse XML"]'))


if __name__ == '__main__':
    main()
