import qrcode
import cv2
import os
from datetime import datetime

def generar_qr(data, filename):
    """Genera un código QR y lo guarda en la carpeta qr_codes/"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')

    filepath = f"qr_codes/{filename}.png"
    img.save(filepath)

    guardar_log(f"Código QR generado: {data} -> {filepath}")

    return filepath

def decodificar_qr(image_path):
    """Decodificaa un código QR de una imagen y retorna los datos"""
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print(f"Datos decodificados: {data}")
        guardar_log(f"Código2 QR decodificado: {data} desde {image_path}")
        return data
    else:
        print("No se pudo decodificar el código QR.")
        return None

def guardar_log(mensaje):
    """Guarda un mensaje en el archivo de log"""
    log_filepath = "logs/qr_log.txt"
    if not os.path.exists('logs'):
        os.makedirs('logs')

    with open(log_filepath, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {mensaje}\n")
