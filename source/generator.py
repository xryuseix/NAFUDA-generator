import cv2
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import fetch
import read_csv
import re
from tqdm import tqdm

def is_japanese(str):
    return True if re.search('[ぁ-んァ-ン]', str) else False 

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
    img2 = cv2.resize(img2,(379,379))
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    large_img = img1
    small_img = img2
    # plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    # アイコン画像の左上の座標を決めて，テンプレート画像に重ねる
    x_offset=69
    y_offset=408
    large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

    max_char = 11 # 枠に収まる最大の文字数
    name_left = 450 # 名前の枠の左端
    name_right = 1340 # 名前の枠の右端
    name_height = 580 # 名前の高さ
    username_size = len(username) # 名前文字数
    font_size = 3.8 # 名前のフォントの大きさ
    font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', 138) # フォントの指定/サイズ
    char_size = 62 # 一文字単位の文字サイズ
    
    if username_size > max_char:
        font_size = 2.7
        char_size = 44
    if is_japanese(username):
        char_size *= 1.5

    # テキスト表示位置
    name_start_pos = ((name_right - name_left) - (username_size * char_size))//2 + name_left
    position = (name_start_pos, name_height)

    img_pil = Image.fromarray(large_img) # 配列の各値を8bit(1byte)整数型(0～255)をPIL Imageに変換。
    draw = ImageDraw.Draw(img_pil) # drawインスタンスを生成

    
    draw.text(position, username, font = font , fill = (0, 0, 0, 0) ) # drawにテキストを記載 fill:色 BGRA (RGB)
    large_img = np.array(img_pil)

    if twitter_id != 'rippro_logo_small':
        cv2.putText(large_img, '@' + twitter_id, (60, 830), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)

    plt.imshow(large_img)
    plt.show()
    plt.savefig('./storage/generated_images/' + username + '.png', bbox_inches='tight', pad_inches = 0.1)
    return large_img

def images():
    image_download = False
    images = []
    csv = read_csv.read_csv()

    for row in tqdm(csv):
        s = row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）']
        s = re.sub('^@', '', s)
        if row['名前またはハンドルネーム（名札で使用します）']=='handlename2':
            row['名前またはハンドルネーム（名札で使用します）']='流流流流'
        row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'] = s
        if image_download:
            fetch.download_images(row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'])
        image = make_image(row['名前またはハンドルネーム（名札で使用します）'], row['Twitter ID（Twitterアイコンを名札の画像に使用します。記入がない場合、画像なしの名札になります）'])
        images.append(image)
    
    return images