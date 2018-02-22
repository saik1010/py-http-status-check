import requests
from bs4 import BeautifulSoup

# アクセスするURL
resp = requests.get("https://www.google.co.jp/")

# BeauttifulSoupを使用してHTML整形
soup = BeautifulSoup(resp.text, 'html.parser')

# aタグからURLを取得し、HTTPリクエストを送る
for link in soup.find_all('a'):

    # URLを取得し、HTTPリクエスト
    url = link.get('href')
    if url is None:
        continue
    elif url == '#':
        continue
    elif url.find('http') == -1:
        continue
    resp = requests.get(url)

    # 結果をCSVに出力する
    f = open('test.csv','a')
    f.write(str(resp.status_code) + ',' + url + '\n')
    f.close()
