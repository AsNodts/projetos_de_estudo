import qrcode #lib que cria o qr
import urllib.request #usada principalmente para abrir e ler URLs, seja em formato HTTP, HTTPS, FTP, etc.

def criar_qrcode(link):
    qr = qrcode.QRCode( # type: ignore
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # type: ignore #diminuir problemas, padrao M não é tao necessario
        box_size=10, #apenas por frescura, nãoé tao necessario caso nao precise expecificar o tamanho
        border=4, #tamanho da borda do qr 
    )
    qr.add_data(link)  # Adiciona o link ao QR Code
    qr.make(fit=True) #molda o tamanho do qrcode para qualquer tela de dispositivo

    img = qr.make_image(fill_color="black", back_color="white")  # Cor do QR Code
    img.save("qrcode.png")  # Salva o QR Code

while True:
    link = input('Quer criar um QrCode para qual site? ').strip()
    if not link:
        print("A entrada está vazia. Por favor, insira uma URL válida.")
        continue
    
    # Verifica se a entrada parece ser uma URL válida
    if not (link.startswith("http://") or link.startswith("https://")):
        print("A URL deve começar com 'http://' ou 'https://'.")
        continue

    try:
        site1 = urllib.request.urlopen(link) #verifica se o site está acessavel pra depois criar o qr
        print(f"Conexão bem-sucedida com {link}")
        criar_qrcode(link)  # Chama a função para criar o QR Code
        print("QR Code criado com sucesso e salvo como 'qrcode.png'")
        break
    except urllib.error.URLError: # type: ignore #caso não seja acessavel
        print("Erro na conexão com a internet ou a URL não foi encontrada. Tente novamente.")
        while True:
            resp = input('Quer continuar? [S]im / [N]ão').strip().upper()[0]
            if resp in ('SN'):
                break
            print('Responda com [S]im ou [N]ão.')
        if resp == 'N':
            break
print('Obrigado por usar o gerador de Qrcode.')