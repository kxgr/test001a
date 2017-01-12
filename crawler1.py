import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages, url):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_colde.text
        #print(plain_text)
        soup_obj = BeautifulSoup(plain_text, "html.parser")
        counter = 0
        for link in soup_obj.find_all('a'):
            counter += 1
            href = link.get('href')
            write_file(str(counter))
            write_file(href)
            print(href)
        page += 1


def write_file(name):
    fo = open('test.txt', 'w')
    fo.write(name)
    fo.write("\n")
    fo.close()


def main():
    url = 'http://www.github.com'
    trade_spider(1, url)


if __name__ == '__main__':
    main()