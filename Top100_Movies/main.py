import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL).text
soup = BeautifulSoup(response, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in movie_tags]

for movie in movies[::-1]:
    print(movie)
