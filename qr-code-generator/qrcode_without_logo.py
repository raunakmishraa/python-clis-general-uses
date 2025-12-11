import qrcode
from PIL import Image


link='https://forms.gle/PoxrY9TmuZb9pGot9' #change the link

QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
QRcode.add_data(link)
QRcode.make()
#Change QR color
QRcolor = '#fa0096'
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="transparent")
save_as_name="D:\\Innovation\\Python_Programs\\Python_CLIs\\entranceWorldQR.png"
QRimg.save(save_as_name)

print("QR Generated !!")
