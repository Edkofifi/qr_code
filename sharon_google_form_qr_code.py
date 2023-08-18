import qrcode

link = "https://forms.gle/AHpGWyFc5HLB62H37"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")  # Save the QR code image as "qrcode.png" or your preferred filename
