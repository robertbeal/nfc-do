# nfc-do

Container for interacting with MFRC522 module on a raspi and performing actions. It is used for (kids) playing music via dlna by using NFC cards.

## Usage

```bash
docker run -d \
    --name=nfc-do \
    --restart on-failure:5 \
    --privileged \
    --net=host \
    --tty \
    -v $HOME/config:/config:ro \
    -v $HOME/data:/data \
    robertbeal/nfc-do
```
