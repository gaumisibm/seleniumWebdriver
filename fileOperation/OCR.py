import easyocr
import cv2
from pylab import rcParams
from IPython.display import Image
def ocrconvertor():
    rcParams['figure.figsize'] = 8, 16
    reader = easyocr.Reader(['en'])
    output = reader.readtext("C:/Users/KumarGaurav/Desktop/screenTest/captcha12.png")
    captcha = output[0][1]
    return captcha, output[0][2]


print(ocrconvertor())