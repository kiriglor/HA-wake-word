FROM python:3.9-slim

# Install dependencies
RUN pip install numpy openwakeword requests

# Copy files
COPY receive_audio.py /app/receive_audio.py
COPY run.sh /app/run.sh

# Set working directory
WORKDIR /app

# Make run.sh executable
RUN chmod +x run.sh

# Entrypoint
CMD ["./run.sh"]
