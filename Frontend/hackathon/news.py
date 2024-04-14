from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_website():
    # Your web scraping code here...
    # For example:
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    data = [{'title': link.getText(), 'link': link.get('href')} for link in links]
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hacker_news')
def hacker_news():
    scraped_data = scrape_website()
    return render_template('newsletter.html', hacker_news=scraped_data)

if __name__ == '__main__':
    app.run(debug=True)
