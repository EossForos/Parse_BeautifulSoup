import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
        print(r.status_code)

def write_csv(data):
    with open('#Namefile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    sourse = soup.find_all('#resurse.html', class_='#name class')
    for sourse in sourses:
        try:
            name = #sourse.find('').text
        except:
            name = ''
        try:
            url = 'site url address' + sourse.find('#').find('#').get('#')
        except:
            url = ''
        try:
            price = sourse.find('#').find('#').text#.replace('€', '$')
        except:
            price = ''

        data = {'name': name,
                'url': url,
                'price': price}
        write_csv(data)

#pagination

def main():
    pattern = 'https://www.your site.html?page={}'
    for i in range(0, 0):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
