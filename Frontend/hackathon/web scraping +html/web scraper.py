import requests
from bs4 import BeautifulSoup
import json

def scrape_hacker_news():
    # Send HTTP request to Y Combinator's news page
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')

    # Extract news article links and subtexts
    links = soup.select('.titleline > a') 
    subtext = soup.select('.subtext')

    # Combine links and subtexts
    hn_data = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 50:
                hn_data.append({'title': title, 'link': href, 'votes': points})

    return hn_data

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Scrape Hacker News
    hn_data = scrape_hacker_news()

    # Save data to JSON file
    save_to_json(hn_data, 'hn_news.json')

    print("Data saved to hn_news.json")
