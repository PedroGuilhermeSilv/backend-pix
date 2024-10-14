from io import BytesIO

import qrcode
import requests
from PIL import Image


# Função para gerar o QR code
def gerar_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill="black", back_color="white")
    return img_qr


# Função para adicionar o QR code no template
def adicionar_qrcode_template(template_url, qrcode_img, posicao):
    # Baixar o template a partir da URL
    response = requests.get(template_url)
    template = Image.open(BytesIO(response.content))

    # Redimensionar o QR code, se necessário
    qrcode_img = qrcode_img.resize((500, 500))  # Exemplo de redimensionamento

    # Colocar o QR code na posição desejada
    template.paste(qrcode_img, posicao)

    # Salvar a imagem final
    template.save("output_template_com_qrcode.png")
    template.show()


# URL do QR code (pode ser dinâmico ou estático)
url_qrcode = "https://s3.tebi.io/aula/asdf3.png"

# URL para o template
template_url = "https://files.stripe.com/links/MDB8YWNjdF8xT1VYdFZBa0JMVmhUdmYxfGZsX3Rlc3RfTmFodWNGeW5lUE1Qd3hEU1FVdmFveGlM00xRrIRRSd"

# Gerar o QR code
qrcode_img = gerar_qrcode(url_qrcode)

# Definir a posição onde o QR code será colocado (exemplo: canto inferior direito)
posicao_qrcode = (320, 495)  # Altere conforme o local onde deseja posicionar

# Adicionar o QR code ao template
adicionar_qrcode_template(template_url, qrcode_img, posicao_qrcode)
