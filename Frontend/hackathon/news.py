from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scrape_hacker_news():
    res = requests.get('https://news.ycombinator.com/news')
    res2 = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(res.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    links2 = soup2.select('.titleline > a')
    subtext2 = soup2.select('.subtext')

    mega_links = links + links2
    mega_subtext = subtext + subtext2

    hn = []
    for idx, item in enumerate(mega_links):
        title = item.getText()
        href = item.get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

@app.route('/')
def newsletter():
    hn_data = scrape_hacker_news()
    return render_template('newsletter.html', hn_data=hn_data)

if __name__ == '__main__':
    app.run(debug=True)
