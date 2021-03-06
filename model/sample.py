from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import base64
import os


class Main(object):
    def __init__(self, url: str):
        """class初期設定"""
        self.url = url
        self.url_title = None
        self.driver = None
        self.soup = None

        self.idx = 0

    def driver_init(self):
        """webdriverの初期設定"""
        op = Options()
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument("--headless")
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver', options=op)

    def driver_wait(self):
        """ページ移動時の関数"""
        selector = 'body'
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def canvas_get(self):
        """canvas内の画像を取得する関数"""
        self.dir_create()
        print('canvas内の画像を取得する')

        canvas_first = self.driver.find_element_by_css_selector(
            '#output')

        base64_first = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                  canvas_first)
        first_png = base64.b64decode(base64_first)

        with open("img/{}/{}.png".format(self.url_title, self.idx), 'wb') as f:
            f.write(first_png)

    def next_page_click(self):
        """次のページに移動する関数"""
        print('次のページに移動する')
        next_page = self.driver.find_element_by_css_selector('#output')
        next_page.click()
        self.idx += 1

    def dir_create(self):
        """保存先フォルダを作成する関数"""
        self.url_title = self.driver.title.split("-")[0].strip()
        # フォルダが存在しない場合のみフォルダを生成する条件文
        if os.path.exists('img') is False:
            os.mkdir('img')
        if os.path.exists('img/' + self.url_title) is False:
            os.mkdir('img/' + self.url_title)
