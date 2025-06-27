<h1 align="center">
  qrclip
</h1>

## Installation 🚏

```console
# clone the repo
$ git clone https://github.com/Louise-h-aa/qrclip.git

# change the working directory to qrclip
$ cd qrclip

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage 🔗

```console
python3 qrclip.py
```

## Automation 📳

> [!IMPORTANT]
> For autonomy in `Linux`, create a service in folder `etc/systemd/system` named [qrclip.service](configs/qrclip.service)

> service text:
```conf
[Unit]
Description=QR Clip Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/qrclip
ExecStart=/usr/bin/python3 /opt/qrclip/qrclip.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

> [!TIP]
> Please note that the `user` (root) on whose behalf you are running and the `directory` (opt/qrclip) can be set by you according to your own
