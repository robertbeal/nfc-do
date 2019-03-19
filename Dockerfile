FROM arm32v6/alpine

WORKDIR /app

RUN apk add --no-cache --virtual=build-dependencies \
      alpine-sdk \
      linux-headers \
      python3-dev \
    && apk add --no-cache \
      curl \
      git \
      python3 \
      wget \
    && python3 -m pip --no-cache-dir install --upgrade \
      pip \
      RPi.GPIO \
      spidev \
    && git clone https://github.com/pimylifeup/MFRC522-python.git --depth 1 \
    && mv MFRC522-python/* ./ \
    && wget -O ./dlnap.py https://raw.githubusercontent.com/cherezov/dlnap/master/dlnap/dlnap.py \
    && apk del --purge build-dependencies \
    && rm -rf /tmp/*

COPY *.py ./

CMD ["python3", "app.py"]