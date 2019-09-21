FROM balenalib/raspberry-pi-alpine

WORKDIR /app

RUN apk add --no-cache --virtual=build-dependencies \
  alpine-sdk \
  linux-headers \
  python3-dev \
  # packages
  && apk add --no-cache \
  curl \
  git \
  python3 \
  wget \
  # pip
  && python3 -m pip --no-cache-dir install --upgrade pip pipenv RPi.GPIO spidev \
  && pipenv install -d \
  # external packages
  && git clone https://github.com/pimylifeup/MFRC522-python.git --depth 1 \
  && mv MFRC522-python/mfrc522 ./ && rm -Rf MFRC522-python \
  && wget -O ./dlnap.py https://raw.githubusercontent.com/cherezov/dlnap/master/dlnap/dlnap.py \
  # cleanup
  && apk del --purge build-dependencies \
  && rm -rf /tmp/*

COPY . .

CMD ["python3", "app.py"]