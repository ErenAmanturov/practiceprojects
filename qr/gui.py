import tkinter as tk

from qrcode.main import QRCode
import qrcode
from PIL import Image, ImageTk

def get_qrcode(event=None):

    user_url = link.get()
    qr = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(user_url)
    qr.make(fit=True)
    image = qr.make_image()
    image = image.convert('RGB')
    image_tk = ImageTk.PhotoImage(image)

    result_label.config(image=image_tk)
    result_label.image = image_tk

root = tk.Tk()
root.title('QRCode Maker')

url_label = tk.Label(root, text='Enter link')
url_label.pack(pady=10)

link = tk.Entry(root, width=50)
link.pack(pady=10)
link.bind('<Return>', get_qrcode)

button = tk.Button(root, text='Generate QRCode', command=get_qrcode)
button.pack(pady=10)

result_label = tk.Label(root)
result_label.pack(pady=10)

root.mainloop()
