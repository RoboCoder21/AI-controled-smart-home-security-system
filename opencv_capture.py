import cv2

def capture_image():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    ret, frame = cap.read()
    if ret:
        filename = f"captured_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Failed to capture image. Check your webcam connection.")
    
    cap.release()

if __name__ == "__main__":
    capture_image()