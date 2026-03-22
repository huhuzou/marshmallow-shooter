from pythonosc import dispatcher, osc_server
import serial
import time

# --- Serial configuration ---
SERIAL_PORT = "/dev/cu.usbmodem1101"  # Change to your Arduino port
BAUD_RATE = 115200

# --- Wekinator output configuration ---
OSC_PATH = "/wek/outputs"
LISTEN_IP = "127.0.0.1"
LISTEN_PORT = 12001

# Open serial connection
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
print("Serial connected:", SERIAL_PORT)

# Callback to handle messages from Wekinator
def handle_wekinator_output(address, *args):
    if len(args) >= 2:
        v1, v2 = args[0], args[1]
        servo1 = int(v1 * 180)
        servo2 = int(v2 * 180)
        msg = f"{servo1},{servo2}\n"
        arduino.write(msg.encode())
        print(f"From Wekinator → Arduino: {msg.strip()}")

# Set up OSC listener
disp = dispatcher.Dispatcher()
disp.map(OSC_PATH, handle_wekinator_output)

# Start OSC server to receive messages
server = osc_server.BlockingOSCUDPServer((LISTEN_IP, LISTEN_PORT), disp)
print(f"Listening for Wekinator output on {LISTEN_IP}:{LISTEN_PORT} ...")
server.serve_forever()
