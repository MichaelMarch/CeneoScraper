# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](htttps://ceneo.pl)

|Skadowa opinii|Selector|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|indentyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja autora|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div[class$="positives"] ~ div.review-feature__item|pros||
|lista wad|div[class$="negatives"] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|user-post__published > time:nth-child(2)\["datetime"\]|purchased||

## Etapy pracy nad projektem
1. Pobranie elementów pojedynczych opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedynczej opinii do jednej zmiennej
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie dodanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    a. utworzenie funkcji do pobierania składowych strony HTML
    b. utworzenie słownika opisującego strukturę opinii wraz z selektoremi poszczególnych elementów
    c. zamiana instrukcji pobierających skłądowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów.