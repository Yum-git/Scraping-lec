from model import lec1, lec2
import time

def lec1_run():
    base_url = 'https://tanihoshii.ichiya-boshi.net/'
    url = 'https://tanihoshii.ichiya-boshi.net/1.html'
    # クラス生成
    Soup = lec1.Main(base_url, url)
    # BeautifulSoupオブジェクトを生成
    Soup.soup_gene()
    # 画像を取得する
    Soup.img_get()
    # 次のページに移動する
    Soup.next_page()
    # 画像を取得する
    Soup.img_get()


def lec2_run():
    url = 'https://vw.mangaz.com/virgo/view/101/i:0'

    Soup = lec2.Main(url)
    Soup.driver_init()
    Soup.driver_wait()
    Soup.canvas_get()
    Soup.nextpage_click()
    time.sleep(1)
    Soup.canvas_get()


# lec1_run()
lec2_run()
