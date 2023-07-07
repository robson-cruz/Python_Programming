import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


response = requests.get(url="https://news.ycombinator.com/").text

soup = BeautifulSoup(response, "html.parser")

# Get all articles and its url links and votes
articles = soup.find_all(name="a", rel="noreferrer")

title = [tag.getText() for tag in articles]
link = [tag.get("href") for tag in articles]
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Most voted article
max_vote_index = article_upvote.index(max(article_upvote))
print(title[max_vote_index])
print(link[max_vote_index], end="\n\n")

# Get comments
subline = soup.find_all(name="span", class_="subline")

comments = [int(re.findall(r"\b(\d+)\s*comments\b", sub.getText())[0]) for sub in subline if re.findall(r"\b(\d+)\s*comments\b", sub.getText())]

data = {
    "article": title,
    "link": link,
    "vote": article_upvote,
    "comment": comments
}

df = pd.DataFrame(data)
df.to_csv("hack_news_articles.csv", index=False)
