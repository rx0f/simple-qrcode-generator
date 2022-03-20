from PIL import Image
import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = 'Data here'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qr.png')