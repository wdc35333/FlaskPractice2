import json
import pandas as pd
import folium

def folium_visual(pred_year_month, value):
    pred_year = int(str(pred_year_month).split("-")[0])
    month = int(str(pred_year_month).split("-")[-1])

    state_temp = f'static/data/predict/{pred_year}예측.csv'
    state_data = pd.read_csv(state_temp, encoding="cp949")
    state_data = state_data[state_data['month'] == month]

    json1 = 'static/data/조사지역.json'
    state_geo = json.load(open(json1, encoding= 'utf-8'))

    m = folium.Map(location = [36, 127], tiles="OpenStreetMap", zoom_start = 6)

    if value == 'temperature':
        legend = '평균온도'
    elif value == 'temp_max':
        legend = '최고온도'
    elif value == 'temp_min':
        legend = '최저온도'

    m.choropleth(
        geo_data = state_geo,
        name='choropleth',
        data = state_data,
        columns = ['KOR_NUM', f'{value}'],
        key_on= 'feature.properties.SIG_NUM',
        fill_color = 'YlGn',
        fill_opacity = 0.9,
        line_opacity = 0.5,
        legend_name = legend
    )

    folium.LayerControl().add_to(m)

    #Save to html
    m.save('static/data/folium_pred_weather.html')