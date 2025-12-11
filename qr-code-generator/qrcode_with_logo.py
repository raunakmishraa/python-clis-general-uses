import qrcode
from PIL import Image

link='https://forms.gle/PoxrY9TmuZb9pGot9' #Replace the link

logo_file="entranceWorldQR.png"  #Replace the logo file
logo = Image.open(logo_file)
basewidth = 100
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
QRcode.add_data(link)
QRcode.make()
QRcolor = '#fa0096'
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="transparent")
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
save_as_name="D:\\Innovation\\Python_Programs\\Python_CLIs\\qrcode.png"
QRimg.save(save_as_name)
print("QR Generated !!")