from flask import Flask, render_template, request
from flask import current_app
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime
import os, joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

app = Flask(__name__)

@app.route('/')
def index():
    menu = {'home':1, 'menu1':0, 'menu2':0}
    # client_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # print(f'Connected to {client_addr}')

    return render_template('index.html', menu = menu)


@app.route('/menu1', methods=['GET', 'POST'])
def menu1():    # 미래의 년도를 입력받아 해당 년도의 기후를 예측하고 해당 기후에 맞는 작물 추천 (folium을 이용한 지도 시각화)
    menu = {'home':0, 'menu1':1, 'menu2':0}
    if request.method == 'GET':
        return render_template('menu1.html', menu = menu)
    else:
        year = request.form['year']
        return render_template('menu1_res.html', menu = menu, year = year)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
