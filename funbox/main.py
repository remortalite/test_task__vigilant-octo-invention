from funbox.db import conn, create_table_links
from flask import Flask, json


app = Flask(__name__)


@app.get("/visited_links")
def visited_links():
    return {
            "domains": [],
            "status": "ok"
            }


if __name__ == "__main__":
    create_table_links()

    app.run()
