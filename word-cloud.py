import jieba
from matplotlib import pylab as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pymysql import *
import json

def get_image(field,targetImageSrc,resImageSrc):
    con = connect(host='localhost', user='root', password='030825', database='cardata', port=3306, charset='utf8mb4')
    cusor = con.cursor()
    sql = f"select manufacturer from carinfo"
    cusor.execute(sql)
    data = cusor.fetchall()

    text = ''
    for i in data:
        if i[0] != '':
            tagArr = i
            for j in tagArr:
                text += str(j)
    cusor.close()
    con.close()
    data_cut = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cut)

    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        font_path='C:/Users/76759/AppData/Local/Microsoft/Windows/Fonts/I.Ming-8.10.ttf',
        mask=img_arr,
        background_color='#04122c'
    )
    wc.generate_from_text(string)
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')

    plt.savefig(targetImageSrc, dpi=800,bbox_inches='tight', pad_inches=-0.1)

get_image('manufacturer', './big-screen-vue-datav-master/public/carcloud.jpeg','./big-screen-vue-datav-master/public/car_cloud.jpg')