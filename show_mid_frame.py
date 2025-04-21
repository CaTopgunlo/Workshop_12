import cv2

def show_mid_frame(video_path):
    # Abrir el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo abrir el video.")
        return

    # Obtener el número total de frames y calcular el frame de la mitad
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    mid_frame_index = total_frames // 2

    # Ir al frame de la mitad
    cap.set(cv2.CAP_PROP_POS_FRAMES, mid_frame_index)
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame.")
        cap.release()
        return

    # Mostrar el frame
    cv2.imshow("Frame de la mitad", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Liberar el video
    cap.release()

# Ruta del video (modifica esta línea con la ruta de tu video)
video_path = "ruta/del/video.mp4"
show_mid_frame(video_path)
