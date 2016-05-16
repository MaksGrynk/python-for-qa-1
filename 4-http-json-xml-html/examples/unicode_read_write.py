# -*- coding: utf-8 -*-

import codecs


def main():
    with codecs.open('unicode.txt', 'r+',
                     encoding='utf-8', errors='ignore') as f:
        content = f.read()
        print(content)
        f.write('компанія епам'.decode('utf-8'))


if __name__ == '__main__':
    main()
