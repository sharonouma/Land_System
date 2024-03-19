import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr =qrcode.make(" http://127.0.0.1:5000?titledeed_id=")
myqr1 =qrcode.make("You don't get to do that")
myqr.save("myqr.png",scale=8)
myqr1.save("myqr1.png",scale=8)


b =decode(Image.open("myqr.png"))
print(b [0] .data .decode("ascii"))