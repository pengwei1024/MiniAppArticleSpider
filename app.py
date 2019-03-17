from flask import Flask, jsonify
from flask import render_template
import sqlite3

DATABASE = 'mini_app.db'
PAGE_SIZE = 10

app = Flask(__name__)


@app.route('/post/<int:page>')
def get_post(page=0):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("select * from articles order by update_time desc limit {},{}".format(
        page * PAGE_SIZE, PAGE_SIZE))
    data = []
    for row in cursor.fetchall():
        item = {'title': row[1], 'href': row[2], 'desc': row[3], 'time': row[9]}
        data.append(item)
    cursor.close()
    return jsonify(data)


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("select * from articles order by update_time desc limit {}".format(PAGE_SIZE))
    data = []
    for row in cursor.fetchall():
        item = {'title': row[1], 'href': row[2], 'desc': row[3], 'time': row[9]}
        data.append(item)
    cursor.close()
    return render_template('index.Jinja2', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
