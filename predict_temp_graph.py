import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import platform

def weather_temp_month(region, predict_month, temp):
    pred_df = pd.read_csv('static/data/2022-2100기후예측.csv', encoding='cp949')
    
        
    years = pred_df[(pred_df['month'] == predict_month) & (pred_df['KOR_NM'] == region)]['year']        # x축값(년도)
    temperatures = pred_df[(pred_df['month'] == predict_month) & (pred_df['KOR_NM'] == region)][temp]   # y축값(온도)

    years_count = len(years.unique())  # 2022년 예측 데이터는 6월부터 있어서 1~5월과 6~12월의 총 년도 수가 다름을 반영하기 위함

    if temp == 'temperature':
        temp_name = '평균기온'
    elif temp == 'temp_max':
        temp_name = '최고기온'
    elif temp == 'temp_min':
        temp_name = '최저기온'
    

    if platform.system() == "Darwin":  # 맥
        plt.rc('font', family='AppleGothic')
    elif platform.system() == "Windows":  # 윈도우
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == "Linux":  # 리눅스 = 코랩
        plt.rc('font', family='Malgun Gothic')

    
    x = np.arange(years_count)
    plt.figure(figsize=(10, 3))
    plt.plot(x, temperatures, label=f'{region}의 {temp_name}')
    plt.ylim(temperatures.min()-0.2, temperatures.max()+0.2)
    plt.xticks(x, years)
    plt.xlabel('년도')
    plt.ylabel('기온')
    plt.legend()
    plt.savefig('static/img/weather_graph.png', bbox_inches='tight')
    plt.close()
    