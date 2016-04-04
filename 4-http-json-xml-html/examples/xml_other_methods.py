
import xml.etree.ElementTree as etree


def main():
    course_xml = etree.parse('course.xml')

    root = course_xml.getroot()

    for module in root.iter('module'):
        print('{} - {}'.format(module.get('id'), module.text.strip()))
    # module1 - Cource Introduction
    # module2 - Introduction to Python
    # module3 - Python Basics
    # module4 - Python Intermediate
    # module5 - HTTP, JSON, XML, HTML

    for module in root.findall('module'):
        print(module)

    for name in root.findall('name'):
        print(name.text.strip())
    # Python for QA

    modules = root.findall('modules')
    module1 = modules[0].find('module')
    print(module1.get('id'))
    # module1


if __name__ == '__main__':
    main()
