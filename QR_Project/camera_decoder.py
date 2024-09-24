import cv2
from utils import guardar_log

def decodificar_desde_camara():
    """Decodifica un código QR usando la cámara en tiempo real"""
    cap = cv2.VideoCapture(0)

    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print(f"Datos del QR: {data}")
            guardar_log(f"Código QR decodificado desde camara: {data}")
            cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Decodificador QR en tiempo real', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    decodificar_desde_camara()
