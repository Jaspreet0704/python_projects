from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/yahoo/news/headings')
def heading():
    news_items = []
    url = "https://www.yahoo.com/news/world/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    articles = soup.find_all("li", class_="stream-item js-stream-content Bgc(t) Pos(r) Mb(24px)") 

    for article in articles:
        headline_tag = article.find("h3")
        link_tag = article.find("a")
        image_tag = article.find("img")

        headline = headline_tag.get_text(strip=True) if headline_tag else "No headline"
        link = link_tag['href'] if link_tag else "No link"
        image = image_tag['src'] if image_tag else "No image"

    
        if image != "No image" and not image.startswith("http"):
            image = f"https://www.yahoo.com{image}"

        news_items.append({"Headline": headline, "Headline link": link, "Image of Headline": image})


    return jsonify(news_items)

if __name__ == "__main__":
    app.run(debug=True)
