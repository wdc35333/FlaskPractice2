import pandas as pd
import ols_pred
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def saveWeatherPredictYear(StartYear,EndYear,Filename):
    df = pd.read_csv(Filename)
    region = sorted(df['조사지역'].unique())
    region.remove('고산')
    region.remove('관악산')
    region.remove('대관령')
    region.remove('흑산도')
    region.remove('문산')
    region.remove('추풍령')

    for i in range(StartYear,EndYear+1):
        reg_pred_list = []
        for j in range(1,13):
            cnt = 0
            for reg in region:
                pred = ols_pred.OLS_model_predict(reg, f"{i}-{j}")
                reg_pred_list.append(cnt)
                reg_pred_list.append(j)
                reg_pred_list.append(reg)
                for k in pred:
                    reg_pred_list.append(k)
                cnt += 1
        reg_pred_array = np.array(reg_pred_list)
        reg_pred_array = reg_pred_array.reshape(-1,6)
        df2 = pd.DataFrame(reg_pred_array, columns=['KOR_NUM', 'month', 'KOR_NM','temperature', 'temp_max', 'temp_min'])
        df2.to_csv(f"{i}예측.csv", mode='w')


    return print("저장이 완료 되었습니다.")
