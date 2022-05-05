from cmath import sin
import requests
import json
from bs4 import BeautifulSoup

#101052360

product_id = input("Please enter id of the product: ")

url = f"https://www.ceneo.pl/{product_id}#tab-reviews"


all_opinions = []

while url:
    response = requests.get(url)

    if not response.status_code == 200:
        print(f"Status code = {response.status_code}")
        break

    page = BeautifulSoup(response.text, "html.parser")
    opinions = page.select("div.js_product-review")
    
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()

        try:
            recomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            recomendation = None

        stars = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text().strip()
        pros = opinion.select("div[class$=\"positives\"] ~ div.review-feature__item")
        pros = [item.get_text() for item in pros]
        cons = opinion.select("div[class$=\"negatives\"] ~ div.review-feature__item")
        cons = [item.get_text() for item in cons]
        useful = opinion.select_one("button.vote-yes > span").get_text().strip()
        useless = opinion.select_one("button.vote-no > span").get_text().strip()
        published = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            purchased = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchased = None

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "recomendation": recomendation,
            "stars": stars,
            "content": content,
            "pros": pros,
            "pros": pros,
            "useful": useful,
            "useless": useless,
            "published": published,
            "purchased": purchased
        }
        all_opinions.append(single_opinion)
    
    try:
        url = "https://ceneo.pl" + page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

with open(f"opinions/opinions_{product_id}.json", "w", encoding="utf-8") as file:
    json.dump(all_opinions, file, indent=4, ensure_ascii=False)
