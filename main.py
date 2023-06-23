import pyqrcode

url = pyqrcode.create('http://www.canbirlik.com')

url.svg('url.svg', scale=8)
url.eps('url.eps', scale=2)
