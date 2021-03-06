#!/usr/bin/env python3
# coding=utf-8
from flask import Flask, request, render_template, jsonify, json
import pymysql

app = Flask(__name__)


@app.route('/scan/<city_name>', methods=['GET'])
def scan(city_name):
    conn = pymysql.connect(
        host='rm-uf61zu38p9t1h913mo.mysql.rds.aliyuncs.com',
        port=3306,
        user='root',
        passwd='hzw123456+-',
        db='weather',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    sql = "select * from weather_today WHERE cityname ='%s'" % (city_name)
    cur.execute(sql)
    results = cur.fetchall()
    # for row in results:
    json_result = {'cityname': results[0]['cityname'], 'week': results[0]['week'],
                   'now_temperature': results[0]['now_temperature'],
                   'weather': results[0]['weather']}
    cur.close()
    conn.commit()
    conn.close()
    return json.dumps(json_result, ensure_ascii=False)


@app.route('/')
def index():
    return render_template('new.html')


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        debug=True
    )
