# Web scraper
from bs4 import BeautifulSoup
import requests

url = 'https://geekhack.org/index.php?topic=82389'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

authors = [author.get_text() for author in soup.select('.post_wrapper .poster h4 a')]
posts = [post.get_text() for post in soup.select('.post_wrapper .inner')]
for author, post in zip(authors, posts):
        if author == "Sneaky Potato":
                print(post)
                print()