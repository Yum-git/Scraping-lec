from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import base64
import os


class Main(object):
    def __init__(self, url: str):
        self.url = url
        self.url_title = None
        self.driver = None
        self.soup = None

        self.idx = 0

    # webdriverの初期設定
    def driver_init(self):
        # どんな環境でもSeleniumで動かせるよー
        op = Options()
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument(
            "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36")
        op.add_argument("--headless")
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver', options=op)

    # ページ移動時の関数
    def driver_wait(self):
        selector = 'body'
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def canvas_get(self):
        self.dir_create()
        print('canvas内の画像を取得する')

        canvas_first = self.driver.find_element_by_css_selector(
            '#book > div.page.first.right > div.page_unit.page_image > canvas')
        canvas_second = self.driver.find_element_by_css_selector(
            '#book > div.page.second.left > div.page_unit.page_image > canvas')

        base64_first = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                  canvas_first)
        base64_second = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                   canvas_second)
        first_png = base64.b64decode(base64_first)
        second_png = base64.b64decode(base64_second)

        with open("img/canvas_{}.png".format(self.idx), 'wb') as f:
            f.write(first_png)
        with open("img/canvas_{}.png".format(self.idx + 1), 'wb') as f:
            f.write(second_png)

    def nextpage_click(self):
        print('次のページに移動する')
        next_page = self.driver.find_element_by_css_selector('.flip.flip-left')
        next_page.click()
        self.idx += 2

    # フォルダを作成する
    def dir_create(self):
        # フォルダが存在しない場合のみフォルダを生成する条件文
        if os.path.exists('img') is False:
            os.mkdir('img')
