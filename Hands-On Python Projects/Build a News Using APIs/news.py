import requests 
from datetime import date, timedelta
query = input("What type of news are you interested in today? \n")
api = "025a4081224d4af2af0696d1a1718edc"

today = date.today()
past_week = today - timedelta(days=7)
url = f"https://newsapi.org/v2/everything?q={query}&from={past_week}&to={today}&sortBy=popularity&apiKey={api}"

r =  requests.get(url)
data = r.json()

articles = data["articles"]

for i, article in enumerate(articles[:10]):
    print(f"News.{i+1} :-{article['title']}")
    print(f"Author:-{article['author']}")
    print(f"description:-{article['description']}\n")
    print(f"for more detail link :- {article['url']}")
    print("-" * 80,"\n")


