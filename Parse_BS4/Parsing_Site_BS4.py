import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
        print(r.status_code)

def write_csv(data):
    with open('Scroutz.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='cf card')
    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''
        try:
            url = 'https://www.skroutz.gr' + li.find('h2').find('a').get('href')
        except:
            url = ''
        try:
            price = li.find('div', class_='price react-component').find('a', class_='js-sku-link sku-link').text#.replace('€', '')
        except:
            price = ''

        data = {'name': name,
                'url': url,
                'price': price}
        write_csv(data)

def main():
    pattern = 'https://www.skroutz.gr/c/40/kinhta-thlefwna/m/28/Samsung.html?page={}'
    for i in range(0, 6):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
