from gnews import GNews

google_news = GNews(language='us', country='US', max_results=10)
news = google_news.get_news('zvo')
for article in news:
    print(f"Заголовок: {article['title']}")
    print(f"Источник: {article['publisher']['title']}")
    print(f"Ссылка: {article['url']}")
    print("-" * 40)

