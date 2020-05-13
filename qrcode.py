# _*_ coding: utf-8 _*_
# _*_ coding: cp950 _*_

# author: Chi-Hsu Chen (css920@gmail.com)
# purpose: a simple python script for scannig and detecting QRCode by PyZBarcode
# datetime: 20200512

import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# 顯示image
def showImg(title,img):
    cv2.imshow(title,img)

# 掃描bar code
def scanQRCode(img):
    barcodes=decode(img)
    print('{} barcodes found in this image'.format(len(barcodes)))
    index=0

    for barcode in barcodes:
        index=index+1

        # 針對抓到的bar code解出內容及類型
        decodetext=barcode.data.decode('utf-8')
        codetype=barcode.type
        text='['+codetype+']'+decodetext
        
        (x,y,width,height)=barcode.rect
        cv2.rectangle(img,(x,y),(x+width,y+height),(0,0,255),3)
        cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

        print('#.{} ================= START ================='.format(index))
        print('x,y,w,h={} text={}'.format((x,y,width,height),text))
        print('#.{} ================= END ================='.format(index))


# main program
# 掃描
img=cv2.imread('D:\\20200513_barcode_test.jpg',cv2.IMREAD_COLOR)
scanQRCode(img)
showImg('QRCode detection',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

