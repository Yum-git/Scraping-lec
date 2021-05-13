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
    try:
        # クラス生成
        Soup = lec2.Main(url)
        # webdriver初期設定
        Soup.driver_init()
        # 指定したurlへ移動+処理
        Soup.driver_wait()
        for _ in range(10):
            # canvasタグ内の画像を取得
            Soup.canvas_get()
            # 次のページに移動
            Soup.next_page_click()
            time.sleep(1)
    except Exception as e:
        print(e)
        Soup.driver.quit()


# lec1_run()
lec2_run()
