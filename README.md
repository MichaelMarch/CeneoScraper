# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](htttps://ceneo.pl)

|Skadowa opinii|Selector|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|indentyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja autora|span.user-post__author-recomendation > em.recommended|recommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div[class$="positives"] ~ div.review-feature__item|pros||
|lista wad|div[class$="negatives"] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|user-post__published > time:nth-child(2)\["datetime"\]|purchased||