import socket
import numpy as np
from openwakeword.model import Model
import requests
import sys

# HA config from add-on options
HA_URL = "http://supervisor/core"
HA_TOKEN = sys.argv[1]  # Passed from run.sh
PORT = int(sys.argv[2])  # Passed from run.sh

# Initialize openWakeWord
oww = Model(wakeword_models=["alexa"], inference_framework="onnx")

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))

print(f"Listening for audio stream on port {PORT}...")
while True:
    data, addr = sock.recvfrom(1280 * 2)  # CHUNK * bytes_per_sample
    audio = np.frombuffer(data, dtype=np.int16)
    prediction = oww.predict(audio)
    if any(pred > 0.5 for pred in prediction.values()):
        print("Wake word detected!")
        headers = {"Authorization": f"Bearer {HA_TOKEN}", "Content-Type": "application/json"}
        requests.post(f"{HA_URL}/api/services/voice_assistant/start_listening", headers=headers)t.SOCK_DGRAM)
