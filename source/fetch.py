import time
from selenium import webdriver
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_images(twitterid):
    twitter_url = 'https://twitter.com/'
    path = './storage/downloaded_images/'
    xpath_string = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/a/div[1]/div[2]/div/img'\

    # ヘッドレスモードで起動
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(twitter_url + twitterid)
    time.sleep(1)
    # 画像情報が入ったURLを取得
    image_url = driver.find_element_by_xpath(xpath_string).get_attribute("src")

    driver.close()
    download_file(image_url, path + twitterid + '.png')
