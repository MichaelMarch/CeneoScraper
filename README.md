# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](htttps://ceneo.pl)

|Skadowa opinii|Selector|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|||
|indentyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja autora|span.user-post__author-recomendation > em.recommended|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet||||
|lista wad||||
|dla ilu osób przydatna|button.vote-yes > span|||
|dla ilu osób nieprzydatna|button.vote-no > span|||
|data wystawienia opinii|user-post__published > time:nth-child(1)\["datetime"\]|||
|data zakupu produktu|user-post__published > time:nth-child(2)\["datetime"\]|||