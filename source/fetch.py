import time
from selenium import webdriver
import os
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

# url = 'https://pbs.twimg.com/profile_images/1160071194390831106/1JLRe3JE_200x200.jpg'
# dst_path = 'py-logo.png'
# download_file(url, dst_path)


url = 'https://twitter.com/ryusei_ishika'
path = './storage/downloaded_images/'
xpath_string = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/a/div[1]/div[2]/div/img'
css_string = 'css-1dbjc4n r-sdzlij r-1p0dtai r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-zchlnj r-ipm5af r-417010'

driver = webdriver.Chrome()

# # ヘッドレスモード
# # options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
# # driver = webdriver.Chrome(options=options)


driver.get(url)
time.sleep(1)

print(driver.find_element_by_xpath(xpath_string).get_attribute("src"))

driver.close()