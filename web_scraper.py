# Web scraper
from bs4 import BeautifulSoup
import requests

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.select('tbody tr')

row = rows[0]

name = row.select_one('.source-title').text.split()

print(name)

# Saving to a file
def save_html(html, path):
    with open(path, 'wb') as f:
        # wb - write bytes
        f.write(html)

save_html(r.content, 'google_com')

# Opening a file
def open_html(path):
    with open(path, 'rb') as f:
        # rb - read bytes
        return f.read()

open_html('google_com')
