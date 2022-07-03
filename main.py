from bs4 import BeautifulSoup
import requests

website_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

content = requests.get(website_url)

soup = BeautifulSoup(content.text, "html.parser")


all_movies = soup.findAll('h3', class_="title")

movie_titles = [movie.getText() for movie in all_movies]

ordered_list = movie_titles[::-1]

for movie in ordered_list:
    print(movie)