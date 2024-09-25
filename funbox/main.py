from flask import Flask, json, request
from urllib.parse import urlparse
from redis import Redis
from datetime import datetime


app = Flask(__name__)
r = Redis('localhost', port=6379)


def normalize_url(url):
    url_parts = urlparse(url)
    if not url_parts.scheme:
        return url_parts.path.split('/')[0]
    return url_parts.netloc


@app.get("/visited_links")
def visited_links_get():
    start_date = request.args.get('from', 0)
    end_date = request.args.get('to', -1)

    links = [x.decode() for x in r.zrange('app:urls', start_date, end_date, withscores=False, byscore=True)]
    return {
            "domains": links,
            "status": "ok"
            }


@app.post("/visited_links")
def visited_links_post():
    data = json.loads(request.data)
    links = data["links"]
    c = 0
    for link in links:
        c += r.zadd('app:urls', {normalize_url(link): int(datetime.timestamp(datetime.now()))})
        print(datetime.timestamp(datetime.now()))
    return {}


if __name__ == "__main__":
    app.run()
