
from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_hacker_news():
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
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 1:
                hn.append({'title': title, 'link': href, 'votes': points})

    sorted_hn = sorted(hn, key=lambda k: k['votes'], reverse=True)

    # Construct HTML content
    html_content = ""
    for news in sorted_hn:
        html_content += f'<div class="news-item">'
        html_content += f'<div class="news-category">Hacker News</div>'
        html_content += f'<div class="news-content">'
        html_content += f'<h2 class="news-title"><a href="{news["link"]}">{news["title"]}</a></h2>'
        html_content += f'<p class="news-summary">Votes: {news["votes"]}</p>'
        html_content += f'</div></div>'

    return html_content

@app.route('/')
def index():
    hacker_news_html = get_hacker_news()
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hacker News</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <header>
            <h1>Hacker News</h1>
        </header>
        <div class="container">
            {hacker_news_html}
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)