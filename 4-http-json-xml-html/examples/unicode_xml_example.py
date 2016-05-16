
import xml.etree.ElementTree as etree


def main():
    # parse xml
    course_xml = etree.parse('feed.xml')

    # get root object
    root = course_xml.getroot()  # <Element 'rss' at 0x102ad4a50>

    title = root[0][0].text
    print(type(title))  # <type 'unicode'>

    # root[0][0].text
    # u'\u0425\u0430\u0431\u0440\u0430\u0445\u0430\u0431\u0440 /
    # \u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u044b\u0435
    # \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'


if __name__ == '__main__':
    main()
