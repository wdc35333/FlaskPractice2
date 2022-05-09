import pandas as pd
import statsmodels.api as sm

def weather_predict(region, pred_year_month, value):
    pred_year = int(str(pred_year_month).split("-")[0])
    month = int(str(pred_year_month).split("-")[-1])
    
    df_weather = pd.read_csv('./static/data/기상데이터전처리_열이름변경.csv')
    df_weather['관측일자'] = pd.to_datetime(df_weather['관측일자'], format='%Y%m%d')
    df_weather['연'] = df_weather['관측일자'].dt.year
    df_weather['월'] = df_weather['관측일자'].dt.month
    df_weather['일'] = df_weather['관측일자'].dt.day
    df_tmp_region = df_weather[df_weather['조사지역'] == region]
    df_weather_region = df_tmp_region.groupby(['조사지역', '관측일자']).mean()


    df_group_mean = df_weather_region.groupby(['연', '월']).mean()
    df_group_mean = df_group_mean.reset_index(drop=False)
    df_month_mean = df_group_mean[df_group_mean['월'] == month]

    for i in df_month_mean.index:
        df_tmp = df_weather_region.loc[(df_weather_region['연'] == df_month_mean.loc[i, '연']) & (df_weather_region['월'] == df_month_mean.loc[i, '월'])]
        temp_max = df_tmp['temp_max'].max()
        temp_min = df_tmp['temp_min'].max()
        df_month_mean.loc[i, 'temp_max'] = temp_max
        df_month_mean.loc[i, 'temp_min'] = temp_min


    df_target = df_month_mean[value]
    X_train2 = pd.DataFrame(df_month_mean[['연']], columns = ['연'])
    y_train2 = df_target.values

    X_train = sm.add_constant(X_train2)
    model = sm.OLS(y_train2, X_train2).fit()
    model.summary()
    pred_value = model.predict(pred_year)
    return pred_value


if __name__ == "__main__":
    weather_predict("속초", '2023-3', 'temp_min')