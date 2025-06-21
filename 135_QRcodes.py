#QR codes with python : tutorial
import pyqrcode
from pyqrcode import QRCode
QR_cd = 'https://www.youtube.com/@tseries'
url = pyqrcode.create(QR_cd)
url.svg("T-series.svg",scale=8)