import qrcode

# Informations du réseau Wi-Fi
ssid = "IRDOFFICE"          # Remplacez par le nom du réseau Wi-Fi
password = "IRDD2018"       # Remplacez par le mot de passe du réseau
security = "WPA"              # Type de sécurité : 'WPA', 'WEP', ou 'nopass'


# Format standard pour les QR Codes Wi-Fi
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

# Générer le QR Code
qr = qrcode.make(wifi_config)

# Sauvegarder l'image
qr.save("wifi_qrcode.png")

print("QR Code Wi-Fi généré avec succès : wifi_qrcode.png")
