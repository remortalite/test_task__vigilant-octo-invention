from funbox.db import create_table_links, select_links
from flask import Flask, json, request
from urllib.parse import urlparse


app = Flask(__name__)


def normalize_url(url):
    url_parts = urlparse(url)
    if not url_parts.scheme:
        return url_parts.path.split('/')[0]
    return url_parts.netloc


@app.get("/visited_links")
def visited_links_get():
    links = select_links()
    return {
            "domains": links,
            "status": "ok"
            }


@app.post("/visited_links")
def visited_links_post():
    data = request.data
    data = json.loads(data)
    links = data["links"]
    normalized_links = set()
    for link in links:
        normalized_links.add(normalize_url(link))
    return {}


if __name__ == "__main__":
    create_table_links()

    app.run()
