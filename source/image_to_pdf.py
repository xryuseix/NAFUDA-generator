# -*- coding:utf-8 -*-
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from PIL import Image

path = "./storage/generated_images/handlename1.png"
image =Image.open(path)
pdf = canvas.Canvas("sample.pdf")

size_rate = 2.5
image = image.resize((int(image.width / size_rate), int(image.height / size_rate)))
pdf.drawInlineImage(image, 30, 200)



#1ページ目を確定
pdf.showPage()

#pdfファイル生成
pdf.save()