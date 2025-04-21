from PIL import Image
import os

def convert_to_black_and_white(image_path, output_path):
    """
    Convierte una imagen a blanco y negro.
    
    :param image_path: Ruta de la imagen de entrada.
    :param output_path: Ruta donde se guardará la imagen en blanco y negro.
    """
    try:
        # Abrir la imagen
        img = Image.open(image_path)
        # Convertir a blanco y negro
        bw_img = img.convert("L")
        # Guardar la imagen convertida
        bw_img.save(output_path)
        print(f"Imagen convertida y guardada en: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ruta de la imagen de entrada
    image_path = input("Introduce la ruta de la imagen: ").strip()
    # Ruta de salida
    output_path = input("Introduce la ruta de salida para la imagen en blanco y negro: ").strip()

    if os.path.exists(image_path):
        convert_to_black_and_white(image_path, output_path)
    else:
        print("La ruta de la imagen no existe. Por favor, verifica e intenta de nuevo.")
