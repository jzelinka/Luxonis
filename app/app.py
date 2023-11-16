from flask import Flask

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import houses_db

app = Flask(__name__)

def scrape_data():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl("test")
    process.start()


def add_to_db(data):
    db = houses_db.db_handler()
    db.create_table()
    for i in data:
        db.insert(i[0], i[1], i[2])


def create_response(data):
    response = ""
    response += '<h1>Real estate from Sreality</h1>'
    response += '<table style="border:1px solid black">'
    response += "<tr><th>Name</th><th>Location</th><th>Image Url</th></tr>"

    for i, row in enumerate(data):
        if i < 500:
            response += "<tr>"
            response += "<td>" + str(i) + "</td>"
            for cell in row:
                response += '<td style="border:1px solid black">' + str(cell) + "</td>"
            response += "</tr>"

    response += "</table>"
    return response


@app.route('/')
def main():
    db = houses_db.db_handler()
    db.create_table()

    return create_response(db.get_rows())

if __name__ == '__main__':
    db = houses_db.db_handler()
    # creating a new database on server startup
    db.delete_table()
    scrape_data()
    app.run(host='0.0.0.0', port=8080)