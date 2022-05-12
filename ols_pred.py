import pandas as pd
import statsmodels.api as sm

def OLS_model_predict(region, pred_year_month):
    pred_year = int(str(pred_year_month).split("-")[0])
    month = int(str(pred_year_month).split("-")[-1])

    df_weather = pd.read_csv('기상데이터 0510 index X.csv')
    df_tmp_region = df_weather[df_weather['조사지역'] == region]
    df_weather_region = df_tmp_region.groupby(['조사지역', '관측일자']).mean()
    df_weather_region = df_weather_region.reset_index(drop=False)

    df_group_mean = df_weather_region.groupby(['연', '월']).mean()
    df_group_mean = df_group_mean.reset_index(drop=False)
    df_month_mean = df_group_mean[df_group_mean['월'] == month]

    for i in df_month_mean.index:
        df_tmp = df_weather_region.loc[(df_weather_region['연'] == df_month_mean.loc[i, '연']) & (df_weather_region['월'] == df_month_mean.loc[i, '월'])]
        temp_max = df_tmp['temp_max'].max()
        temp_min = df_tmp['temp_min'].min()
        df_month_mean.loc[i, 'temp_max'] = temp_max
        df_month_mean.loc[i, 'temp_min'] = temp_min

    pred_list = []
    for value in df_month_mean.columns[2: -2]:
        df_target = df_month_mean[value]
        X_train2 = pd.DataFrame(df_month_mean[['연']], columns = ['연'])
        y_train2 = df_target.values

        # import statsmodels.api as sm
        X_train = sm.add_constant(X_train2)
        model = sm.OLS(y_train2, X_train2).fit()
        pred_value = model.predict(pred_year)
        pred_list.append([region, float(pred_value)])
    
    # print(f'\t\t\t{region}의 {month}월 {pred_year}의 예측값:')
    # print(pred_list)
    return pred_list

if __name__ == "__main__":
    OLS_model_predict("속초", '2023-3')