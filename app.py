import os
import re

from flask import Flask, render_template
import requests

app = Flask(__name__)

status_url = os.getenv("STATUS_URL")


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


def get_data(url):
    data = requests.get(status_url)
    data = data.text
    result = {}

    match1 = re.search(r'Active connections:\s+(\d+)', data)
    match2 = re.search(r'\s*(\d+)\s+(\d+)\s+(\d+)', data)
    match3 = re.search(r'Reading:\s*(\d+)\s*Writing:\s*(\d+)\s*'
        'Waiting:\s*(\d+)', data)
    if not match1 or not match2 or not match3:
        raise Exception('Unable to parse %s' % url)

    result['connections'] = int(match1.group(1))

    result['accepted'] = int(match2.group(1))
    result['handled'] = int(match2.group(2))
    result['requests'] = int(match2.group(3))

    result['reading'] = int(match3.group(1))
    result['writing'] = int(match3.group(2))
    result['waiting'] = int(match3.group(3))

    return result


@app.route("/status")
def status():
    return get_data(status_url)


if __name__ == '__main__':
    app.run("0.0.0.0")
