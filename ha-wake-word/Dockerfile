ARG BUILD_FROM
FROM $BUILD_FROM
FROM python:3.10-slim
RUN pip install numpy openwakeword==0.6.0 onnxruntime==1.16.3 requests
COPY receive_audio.py /app
COPY run.sh /app
WORKDIR /app
RUN chmod a+x /run.sh
CMD ["/run.sh"]
