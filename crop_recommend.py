import json
import folium
import folium as m
import pandas as pd
def crop_recommend(year):
    crop_df = pd.read_csv('static/data/2023-2100년_작물예측.csv', encoding='cp949')
    map_df = pd.read_csv('static/data/위도경도.csv', encoding='cp949')
    crop_df2 = crop_df[crop_df['관측년도'] == year]

    crop_map = m.Map(location = [36.5, 128], tiles="OpenStreetMap", zoom_start = 6.5)
    with open('./static/data/조사지역.json',mode='rt',encoding='utf-8') as f:
        geo = json.loads(f.read())
        f.close()
    
    border = m.GeoJson(
        geo,
        name='korea_municipalities'
    )
    border.add_to(crop_map)

    for i in range(len(map_df)):
        tooltip = map_df.loc[i]['조사지역']
        for row_index, crop in crop_df2.iterrows():
            if crop['조사지역'] == map_df.loc[i]['조사지역']:
                
                popup_msg = f'<br>1순위:{crop["1"]}<br>2순위:{crop["2"]}<br>3순위:{crop["3"]}'
                popup = m.Popup(popup_msg,min_width = 150, max_width=150)
                marker = m.Marker([map_df.loc[i]['위도'], map_df.loc[i]['경도']], icon= m.Icon(color='blue'), tooltip=tooltip, popup=popup)
                marker.add_to(crop_map)

    crop_map.save('static/data/folium_crop.html')