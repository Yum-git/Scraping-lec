import requests
from bs4 import BeautifulSoup
import time
import os


class Main(object):
    # 初期設定
    def __init__(self, base_url: str, url: str):
        self.base_url = base_url
        self.url = url
        self.url_title = None
        self.soup = None

    # BeautifulSoupオブジェクトを生成
    def soup_gene(self):
        # webサイトのデータを取得する
        response = requests.get(self.url)
        response.encoding = response.apparent_encoding

        # 取得したデータを扱えるデータにパースする
        self.soup = BeautifulSoup(response.text, 'lxml')
        self.soup_title()

    # タイトルを取得する
    def soup_title(self):
        # ページのタイトルを取得する
        self.url_title = self.soup.select_one('title').getText()
        # 同じページ名なので特殊な書き方をする
        # 普通はこんな書き方しなくてもいいです
        self.url_title += self.soup.select_one('h1').getText()
        # imgを保存する際のフォルダを生成する
        self.dir_create()

    # フォルダを作成する
    def dir_create(self):
        # フォルダが存在しない場合のみフォルダを生成する条件文
        if os.path.exists('img') is False:
            os.mkdir('img')
        if os.path.exists('img/' + self.url_title) is False:
            os.mkdir('img/' + self.url_title)

    # ページ移動が行われた際に行う関数
    def change_url(self, url: str):
        # 探査urlを変える
        self.url = url
        # BeautifulSoupオブジェクトを生成する
        self.soup_gene()

    # 画像を取得する
    def img_get(self):
        print('画像を取得')
        print()

        idx = 0
        # 画像を抽出する
        for img_soup in self.soup.select('img'):
            # 画像urlを抽出する
            img_url = self.base_url + img_soup.get('src')
            print(idx, '枚目', img_url)
            # 画像をバイナリデータにて取得する
            response = requests.get(img_url)
            # 画像を保存する
            with open("img/" + self.url_title + "/{}.jpg".format(idx), "wb") as f:
                f.write(response.content)
            idx += 1
            # 取得間隔を調整する
            time.sleep(1)

    # 次のページに移動できる
    def next_page(self):
        print('次のページに移動する')
        print()

        # 全てのaタグを抽出する
        for a_tag in self.soup.select('a'):
            a_title = a_tag.getText()
            if a_title == '次のページ':
                a_url = a_tag.get('href')
                self.change_url(self.base_url + a_url)
                break

    # タグを好きに変更できる関数
    def practice_print(self):
        print('練習用関数')
        print()
        # ↓ここを好きに書き換える↓
        for tag_ in self.soup.select(''):
            print(tag_)


base_url = 'https://tanihoshii.ichiya-boshi.net/'
url = 'https://tanihoshii.ichiya-boshi.net/1.html'
# クラス生成
Soup = Main(base_url, url)

# BeautifulSoupオブジェクトを生成
Soup.soup_gene()

# 画像を取得する
Soup.img_get()

# 次のページに移動する
Soup.next_page()

# 画像を取得する
Soup.img_get()
