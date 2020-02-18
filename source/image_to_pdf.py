# -*- coding:utf-8 -*-
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from PIL import Image
import generator

path = "./storage/generated_images/handlename1.png"
generator.images()
image = Image.open(path)
pdf = canvas.Canvas("sample.pdf")
# image = images[1]
# import matplotlib.pyplot as plt
# plt.imshow(image)
# plt.show()
# size_rate = 2.5
# image = image.resize((int(image.width / size_rate), int(image.height / size_rate)))

pdf.drawInlineImage(image, 30, 200, width=259.2, height=172.1)



#1ページ目を確定
pdf.showPage()

#pdfファイル生成
pdf.save()