import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

def my_wordcloud(keyword):
    '''
    tag 파일을 넣으면 워드클라우드와 상위 10개 단어 각각 튜플형태(단어, 빈도수)로 출력 
    '''
    file = f"static/data/crawling/instagram_tag_{keyword}.csv"
    df = pd.read_csv(file)
    df.value_counts()
    text = df.tag.values
    morph_cnt = Counter(text)
    morph_txt = morph_cnt.most_common()
    morph_txt_up = [tc for tc in morph_txt if tc[1] >= 10]

    morph_txt_up2 = dict(morph_txt_up)


    wordcloud = WordCloud(font_path = "AppleGothic", 
                        background_color='white', 
                        width=1000, height=1000,
                        max_words=50, max_font_size=200)


    # 틱셔너리 구조의 데이터를 이용해 워크클라우드 출력
    wc = wordcloud.generate_from_frequencies(morph_txt_up2)
    plt.figure(figsize=(6, 6), linewidth=2)
    plt.imshow(wc)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.savefig("static/img/wordcloud.png",edgecolor='blue')
    
    

    # 상위 10개 출력
    # for i in Counter(df.tag).most_common()[:10]:
    #     print(i)