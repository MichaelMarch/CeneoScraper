import requests

from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/101052360"
response = requests.get(url)


page = BeautifulSoup(response.text, "html.parser")

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recomendation = opinion.select_one("span.user-post__author-recomendation > em.recommended").get_text()
stars = opinion.select_one("span.user-post__score-count").get_text()
content = opinion.select_one("div.user-post__text").get_text()
pros = opinion.select_one("div[class$=\"positives\"] ~ div.review-feature__item").get_text()
cons = opinion.select_one("div[class$=\"positives\"] ~ div.review-feature__item").get_text()
useful = opinion.select_one("button.vote-yes > span").get_text()
useless = opinion.select_one("button.vote-no > span").get_text()
published = opinion.select_one("user-post__published > time:nth-child(1)")["datetime"]
purchased = opinion.select_one("user-post__published > time:nth-child(2)")["datetime"]

