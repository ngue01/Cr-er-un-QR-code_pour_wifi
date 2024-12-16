# Cr-er-un-QR-code_pour_wifi
Code python 🐍 pour générer QR_code_wifi

# Générateur de QR Code pour Wi-Fi

Ce projet propose deux scripts Python permettant de générer des QR Codes pour un point d'accès Wi-Fi. Ces QR Codes peuvent être scannés pour se connecter automatiquement au réseau sans avoir à saisir manuellement le mot de passe.

## Fonctionnalités
1. **QR Code Wi-Fi sans nom du réseau (SSID) :**
   - Génère un QR Code simple contenant les informations du point d'accès Wi-Fi (SSID, mot de passe, type de sécurité).
   - Le QR Code est sauvegardé sous forme d'image.

2. **QR Code Wi-Fi avec le nom du réseau (SSID) affiché :**
   - Génère un QR Code contenant les informations Wi-Fi.
   - Affiche également le nom du réseau (SSID) en texte en dessous du QR Code.
   - Le résultat est une image plus descriptive.

---

## Prérequis

Assurez-vous d'avoir installé Python 3 et les bibliothèques nécessaires :

```bash
pip install qrcode[pil]
pip install pillow
```

---

## Utilisation des Scripts

### **1. QR Code Wi-Fi sans nom**
Ce script génère un QR Code simple pour un point d'accès Wi-Fi.

#### **Code principal :**
```python
import qrcode

# Informations du réseau Wi-Fi
ssid = "NomDuReseau"         # Remplacez par le SSID du réseau
password = "MotDePasse"      # Remplacez par le mot de passe
security = "WPA"             # Type de sécurité : WPA, WEP ou nopass

# Format standard pour un QR Code Wi-Fi
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

# Générer le QR Code
qr = qrcode.make(wifi_config)

# Sauvegarder l'image
qr.save("wifi_qrcode.png")

print("QR Code Wi-Fi généré avec succès : wifi_qrcode.png")
```

#### **Exécution :**
```bash
python qr_code_simple.py
```

#### **Sortie :**
Un fichier **`wifi_qrcode.png`** sera généré dans le répertoire courant.

---

### **2. QR Code Wi-Fi avec le nom affiché**
Ce script génère un QR Code et ajoute le nom du réseau Wi-Fi (SSID) sous forme de texte en dessous du QR Code.

#### **Code principal :**
```python
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Informations Wi-Fi
ssid = "NomDuReseau"         # Nom du réseau Wi-Fi
password = "MotDePasse"      # Mot de passe
security = "WPA"             # Type de sécurité : WPA, WEP ou nopass

# Format standard pour le QR Code Wi-Fi
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

# Générer le QR Code
qr = qrcode.make(wifi_config)
qr = qr.convert("RGB")  # Convertir en mode RGB pour la compatibilité

# Ajouter le texte (SSID) sous le QR Code
text = f"Wi-Fi: {ssid}"
font_size = 20

try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

qr_width, qr_height = qr.size
text_bbox = font.getbbox(text)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

total_height = qr_height + text_height + 10
new_image = Image.new("RGB", (qr_width, total_height), "white")
new_image.paste(qr, (0, 0))

draw = ImageDraw.Draw(new_image)
text_x = (qr_width - text_width) // 2
text_y = qr_height + 5
draw.text((text_x, text_y), text, fill="black", font=font)

new_image.save("wifi_qrcode_with_text.png")

print("QR Code Wi-Fi généré avec succès : wifi_qrcode_with_text.png")
```

#### **Exécution :**
```bash
python qr_code_with_name.py
```

#### **Sortie :**
Un fichier **`wifi_qrcode_with_text.png`** sera généré, contenant le QR Code avec le SSID affiché en dessous.

---

## Résultats attendus

### 1. **QR Code Wi-Fi sans nom :**
![QR Code Wi-Fi simple](https://via.placeholder.com/200x200?text=QR+Code+Wi-Fi)

### 2. **QR Code Wi-Fi avec nom :**
![QR Code avec nom Wi-Fi](https://via.placeholder.com/200x250?text=QR+Code+et+Nom)

---

## Améliorations possibles
- Ajout d'une interface graphique pour générer les QR Codes.
- Support multilingue pour l'affichage des noms.
- Génération automatique de plusieurs QR Codes pour différents réseaux.

---

## Contributions
Les contributions sont les bienvenues ! Si vous avez des idées ou des suggestions, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

---

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
