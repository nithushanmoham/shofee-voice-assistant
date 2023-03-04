import pyqrcode
url='https://www.youtube.com/watch?v=hQdqL6RD42Q&t=50s'
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)
