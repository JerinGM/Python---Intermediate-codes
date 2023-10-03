import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text
#print(data)

soup = BeautifulSoup(data, "html.parser")
list_of_movies = soup.find_all(name="h3", class_="title")

# print(list_of_movies[0].getText())
length = len(list_of_movies)
# print(length)
for i in range (length-1, -1, -1):
    try:
        with open("movies.txt", mode="a", encoding="utf-8") as file:
            file.write(str(list_of_movies[i].getText()) + "\n")
    except FileNotFoundError:
        with open("movies.txt", mode="w", encoding="utf-8") as file:
            file.write(str(list_of_movies[i].getText()) + "\n")


