import qrcode
data = input("Enter your URL: ")
a = input("Enter a name you want to have it on QR Code: ")
filename = a + ".png"
img = qrcode.make(data)
img.save(filename)