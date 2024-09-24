from utils import generar_qr, decodificar_qr


def main():
    print("Bienvenido al generador y decodificador de códigos QR")

    while True:
        print("\nSelecciona una opción:")
        print("1. Generar código QR")
        print("2. Decodificar código QR desde una imagen")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            data = input("Ingresa los datos para el código QR: ")
            filename = input("Ingresa el nombre del archivo para guardar el código QR: ")
            generar_qr(data, filename)
            print(f"Código QR guardado como {filename}.png en la carpeta qr_codes/")

        elif opcion == '2':
            filepath = input("Ingresaa la ruta de la imagen QR para decodificar: ")
            data = decodificar_qr(filepath)
            if data:
                print(f"Datos decodificados: {data}")

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
