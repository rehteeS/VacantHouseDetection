from selenium import webdriver
from selenium.webdriver.common.keys import Keys
''' やること：例外処理を実装する、使用制限が来たらスリープできるようにする '''
''' headingがわかれば、直前の家の向きは必要ない(heading±90°で家の向きになる) '''


import time
import csv
import json

''' SVinfoは、dict型でキーをパノラマID、要素を['家の方向',[['隣接ID１','隣接ID１の方向'],...] ]にする　'''
SVinfo = []
'''isVisitedは、dict型でキーにパノラマIDを指定する'''
isVisited = {}

''' 前回までのデータを読み込む '''
with open('SVinfo1.csv','r') as f1:
    dataReader = csv.reader(f1)
    for row in dataReader :
        isVisited.update({row[0]:True})

init_Cpano = []
with open('Current_pano.csv','r') as f2:
    dataReader = csv.reader(f2)
    for row in dataReader:
        print(row)
        init_Cpano = row


print(isVisited)

'''初期設定の値'''
init_lat = '42.6562043'
init_lng = '141.6189868'
init_pano = 'Dp4fYPJM2SkkcO7fs-eZGAQ'




''' キューは、.appendでエンキュー、.pop(0)でデキュー '''
Queue = init_Cpano


driver = webdriver.Chrome(executable_path = "./chromedriver")
driver.get("file:///Users/ooehirotaka/Desktop/streetview_test/index.html")

'''初期座標の設定（どこでもOK）'''
driver.execute_script("initFunc("+init_lat+","+init_lng+"); ")
time.sleep(1)


print (Queue)


with open('SVinfo1.csv','a') as f3:
    writer = csv.writer(f3, lineterminator='\n')
    ''' SVinfo[current_pano][1]に隣接ノードの情報を格納していく '''
    ''' 隣接するパノラマIDをエンキューしていく '''
    while len(Queue) != 0 :
        print(len(isVisited))
        if len(isVisited) > 1100:
            break
        current_pano = Queue.pop(0)
        print (current_pano)
        driver.execute_script('streetViewPanorama.setPano("'+current_pano+'");')
        time.sleep(0.5)
        result = driver.execute_script("return GL();")
        data = json.loads(result)
        print(data)
        print(Queue)
        for node in data :
            if node['pano'] not in isVisited :
                isVisited.update({node['pano']:True})
            elif isVisited[node['pano']] == True :
                continue
            elif isVisited[node['pano']] != True :
                isVisited[node['pano']] = True
            Queue.append(node['pano'])
            SVinfo = [node['pano'],node['heading']]
            writer.writerow(SVinfo)

with open('Current_pano.csv','w') as f4:
    writer = csv.writer(f4, lineterminator='\n')
    writer.writerow(Queue)


input()

# 終了
driver.close()
