from flask import Flask, render_template
from bs4 import BeautifulSoup
import json
import urllib3
import NYTsecrets

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/<name>')
def name(name):
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def headlines(name):
    url = f"https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={NYTsecrets.api_key}"
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    html_doc = response.data.decode('utf-8')
    soup = BeautifulSoup(html_doc)
    json_object = json.loads(soup.p.text)
    h = []
    for i in range(5):
        h.append(json_object['results'][i]['title'])
    return render_template('headlines.html', name=name, h1=h[0], h2=h[1], h3=h[2], h4=h[3], h5=h[4])


if __name__ == '__main__':  
    app.run(debug=True)