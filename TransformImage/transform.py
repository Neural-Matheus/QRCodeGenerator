import qrcode
from PIL import Image

def transform(link):
    """
    Cria um QR Code a partir de um link e salva a imagem como 'ig-url.png'.

    Args:
        link (str): O link que será convertido em um QR Code.

    Returns:
        None
    """
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(link)
    qr.make(fit=True)

    image = qr.make_image(fill_color="purple", back_color="white")
    image.save("ig-url.png")

# Solicita ao usuário que digite o link para criar um QR Code
print('Digite o link que deseja criar um QRCode: ', end='')
linkI = input()

# Chama a função transform para criar o QR Code
transform(linkI)