
from lxml import html


def main():
    dom = html.parse(('http://www.amazon.com/Apple-MH0W2LL-10-Inch-Retina-'
                      'Display/dp/B00OTWOAAQ/ref=sr_1_1?s=pc&ie=UTF8&'
                      'qid=1459799371&sr=1-1&keywords=ipad'))
    title = dom.find('//*[@id="productTitle"]')
    print(title.text)


if __name__ == '__main__':
    main()


