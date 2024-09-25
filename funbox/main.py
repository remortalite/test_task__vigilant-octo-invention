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
    start_date = request.args.get('from', '-inf')
    end_date = request.args.get('to', '+inf')

    links = [x.decode() for x in r.zrange('app:urls', start_date, end_date, withscores=False, byscore=True)]
    return {
            "domains": links,
            "status": "ok"
            }


@app.post("/visited_links")
def visited_links_post():
    data = json.loads(request.data)
    links = data["links"]
    ts_now = int(datetime.timestamp(datetime.now()))
    for link in links:
        r.zadd('app:urls', {normalize_url(link): ts_now})
    return {}


if __name__ == "__main__":
    app.run()
