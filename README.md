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

## Etapy pracy nad projektem strukturalnym
1. Pobranie elementów pojedynczych opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedynczej opinii do jednej zmiennej
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie dodanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    1. utworzenie funkcji do pobierania składowych strony HTML
    2. utworzenie słownika opisującego strukturę opinii wraz z selektoremi 3oszczególnych elementów
    4. zamiana instrukcji pobierających skłądowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów.
7. Analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie
        2. liczba opinii w których autor podał listę zalet produktu
        3. liczba opinii w których autor podał listę wad produktu
        4. średnia ocena produktu
    3. przygotowania wykresów na podstawie zawartości opinii
        1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen (liczba gwiazdek)