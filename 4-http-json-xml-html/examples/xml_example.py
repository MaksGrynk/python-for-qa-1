
import xml.etree.ElementTree as etree


def main():
    # parse xml
    course_xml = etree.parse('course.xml')

    # get root object
    root = course_xml.getroot()  # <Element 'course' at 0x10afd48d0>
    print(root)

    # Elements Are Lists
    for child in root:
        print(child)  # <Element 'name' at 0x1053de910>, <Element 'modules' at 0x1053de950>

    # Attributes Are Dictonaries
    modules = root[1]
    for module in modules:
        print(module.attrib)  # {'id': 'module1'}, {'id': 'module2'} ...

    module4 = modules[4]
    print(module4.text.strip())  # HTTP, JSON, XML, HTML


if __name__ == '__main__':
    main()
