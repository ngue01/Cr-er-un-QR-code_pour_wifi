import qrcode
from PIL import Image, ImageDraw, ImageFont

# Informations Wi-Fi
ssid = "IRDOFFICE"          # Remplacez par le nom du réseau Wi-Fi
password = "IRDD2018"       # Remplacez par le mot de passe du réseau
security = "WPA"              # Type de sécurité : 'WPA', 'WEP', ou 'nopass'

# Format standard pour le QR Code Wi-Fi
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

# Générer le QR Code
qr = qrcode.make(wifi_config)

# Convertir le QR Code au mode RGB
qr = qr.convert("RGB")

# Ajouter le texte (SSID) sous le QR Code
# Taille du texte et police
text = f"Wi-Fi: {ssid}"
font_size = 20

# Charger une police système (ou une police personnalisée si disponible)
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Dimensions du QR Code
qr_width, qr_height = qr.size

# Utilisation de getbbox() pour obtenir la taille du texte
text_bbox = font.getbbox(text)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Créer une nouvelle image avec espace pour le texte
total_height = qr_height + text_height + 10  # Ajout de 10 pixels pour l'espacement
new_image = Image.new("RGB", (qr_width, total_height), "white")

# Dessiner le QR Code sur l'image
new_image.paste(qr, (0, 0))

# Dessiner le texte sous le QR Code
draw = ImageDraw.Draw(new_image)
text_x = (qr_width - text_width) // 2  # Centrer le texte horizontalement
text_y = qr_height + 5  # Position verticale sous le QR Code
draw.text((text_x, text_y), text, fill="black", font=font)

# Sauvegarder l'image
new_image.save("wifi_qrcode_with_text.png")

print("QR Code Wi-Fi généré avec succès : wifi_qrcode_with_text.png")
