import qrcode

data = "Don't forget to subscribe"

mod_qrcode = qrcode.QRCode(
  version=2, box_size=5,
  border=1
)
mod_qrcode.add_data(data)
mod_qrcode.make(fit=True)
img = mod_qrcode.make_image(fill_color='blue', back_color='yellow')

img.save('/Users/sean/Desktop/myqrcode1.png')