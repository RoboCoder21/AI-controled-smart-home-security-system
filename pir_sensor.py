import serial
import subprocess
import time

SERIAL_PORT = 'COM12'  # Change to your Arduino port
DISTANCE_THRESHOLD = 50  # cm, adjust as needed

ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

prev_detected = False

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line.isdigit():
            distance = int(line)
            print(f"Distance: {distance} cm")
            detected = distance < DISTANCE_THRESHOLD

            if detected and not prev_detected:
                print("Object detected within range! Capturing image...")
                subprocess.run(["python", "opencv_capture.py"])
            elif not detected and prev_detected:
                print("Object moved out of range.")

            prev_detected = detected

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated.")
    ser.close()