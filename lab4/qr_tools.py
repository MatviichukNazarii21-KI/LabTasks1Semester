import qrcode


def create_qr():
    text = "Мій навчальний проєкт Python"
    image = qrcode.make(text)
    image.save("student_qr.png")
    print("QR-код збережено у student_qr.png")