import cv2
import matplotlib.pyplot as plt
import numpy as np
import fetch
import read_csv
import re
from tqdm import tqdm


def make_image(username, twitter_id = 'rippro_logo_small'):
    path = "./storage/default_images/template.png"
    if twitter_id == 'rippro_logo_small':
        folder = "default_images"
    else:
        folder = "downloaded_images"

    icon = "./storage/" + folder + "/" + twitter_id + ".png"
    
    # 画像の読み込み
    img1 = cv2.imread(path)
    img2 = cv2.imread(icon)
    fig = plt.imshow(img1)
    plt.imshow(img2)
    
    # アイコン画像のサイズ変更
    img2 = cv2.resize(img2,(190,190))
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    large_img = img1
    small_img = img2
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    # アイコン画像の左上の座標を決めて，テンプレート画像に重ねる
    x_offset=35
    y_offset=204
    large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

    max_char = 11 # 枠に収まる最大の文字数
    name_left = 240 # 名前の枠の左端
    name_right = 670 # 名前の枠の右端
    username_size = len(username) # 名前文字数
    font_size = 2.0 # 名前のフォントの大きさ
    char_size = 31 # 一文字単位の文字サイズ
    if username_size > max_char:
        font_size = 1.5
        char_size = 23

    name_start_pos = ((name_right - name_left) - (username_size * char_size))//2 + name_left
    cv2.putText(large_img, username, (name_start_pos, 340), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)
    if twitter_id != 'rippro_logo_small':
        cv2.putText(large_img, '@' + twitter_id, (30, 415), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

    plt.imshow(large_img)
    # plt.show()
    plt.savefig('./storage/generated_images/' + username + '.png', bbox_inches='tight', pad_inches = 0)

csv = read_csv.read_csv()

for row in tqdm(csv):
    s = row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）']
    s = re.sub('^@', '', s)
    row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'] = s
    # print(s)
    fetch.download_images(row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'])
    make_image(row['名前またはハンドルネーム（名札で使用します）'], row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'])