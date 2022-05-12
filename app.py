from flask import Flask, render_template, request
from flask import current_app
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from folium_kr import folium_visual 
import pred_model

app = Flask(__name__)

@app.route('/')
def index():
    menu = {'home':1, 'menu1':0, 'menu2':0, 'menu3':0}
    # client_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # print(f'Connected to {client_addr}')

    return render_template('index.html', menu = menu)


@app.route('/menu1', methods=['GET', 'POST'])
def menu1():    # 미래의 년도를 입력받아 해당 년도의 기후를 예측
    menu = {'home':0, 'menu1':1, 'menu2':0, 'menu3':0}
    if request.method == 'GET':
        return render_template('menu1.html', menu = menu)
    else:
        month = request.form['month']
        region = request.form['region']
        temp = request.form['temp']
        pred_value = pred_model.weather_predict(region,str(month), temp)
        return render_template('menu1_res.html', menu = menu, month = month, region=region, temp=temp, result = pred_value)

@app.route('/menu2', methods=['GET', 'POST'])
def menu2():    # 미래의 년도를 입력받아 해당 년도의 기후를 예측 후 시각화
    menu = {'home':0, 'menu1':0, 'menu2':1, 'menu3':0}
    if request.method == 'GET':
        return render_template('menu2.html', menu = menu)
    else:
        month = request.form['month']
        temp = request.form['temp']
        folium_visual(month, temp)
        return render_template('menu2_res.html', menu = menu, month = month, temp=temp )

@app.route('/menu3')
def menu3():     # 미래의 년도를 입력받아 해당 년도의 기후를 예측하고 해당 기후에 맞는 작물 추천 (folium을 이용한 지도 시각화)
    menu = {'home':0, 'menu1':0, 'menu2':0, 'menu3':1}
    return render_template('menu3.html', menu = menu)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
