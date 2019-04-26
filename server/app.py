from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from flask import jsonify
import pprint

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/rank', methods=['GET', 'POST'])
def parser() :
    print("gogo")
    page = 1
    rank = []
    color = []
    comment = []
    name = []
    pro = []
    per = []
    i = 0
    while page <= 3:
        url = 'https://www.acmicpc.net/school/ranklist/426/' + str(page)
        code = requests.get(url)
        text = code.text
        soup = BeautifulSoup(text, 'lxml')
        for id in soup.select('tbody > tr > td'):
            if(i % 6 == 0) : #rank
                    rank += [id.string]
            if(i % 6 == 1) : #color, name
                name += [id.string]
                if(id.select('span') != []):
                    if(id.select('span')[0].get('class') == ['']):
                        color += ['user-normal']
                    else :
                        color += id.select('span')[0].get('class')
                        # print(id.select('span')[0].get('class'))
                else :
                        color += ['user-normal']
            if(i % 6 == 2) : #comment
                comment += [id.string]
            if(i % 6 == 3) : #problem
                pro += [id.string]
            if(i % 6 == 5) : #per
                per += [id.string]
            i += 1
        page += 1
    # print(color)
    ret = []
    for i in range(i//6):
        ret += [{
            'rank': rank[i],
            'name': name[i],
            'color': color[i][5:],
            'comment': comment[i],
            'pro': pro[i],
            'per': per[i],
            'url': 'https://www.acmicpc.net/user/' + name[i]
        }]
    pprint.pprint(ret)
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
