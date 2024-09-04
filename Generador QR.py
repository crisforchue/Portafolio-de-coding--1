import qrcode
import qrcode.constants #Sirve para modificar ciertos campos del QR

qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=7,
                   border=2) #Modificacion del codigo QR.

qr.add_data('https://www.datachar.com') #Agregar a la pagina que va dirigida el QR.
qr.make(fit=True) #Ajustar tamano

img = qr.make_image(fill_color='black', back_color='white')
img.save('datacharQR.png') #Crear y modificar la imagenes del QR. 