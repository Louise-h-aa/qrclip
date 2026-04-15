<h1 align="center">
  qrclip
</h1>

<div align="center">

<strong>Язык: </strong>
<a href="./README.zh.md">🇨🇳 中文</a> |
<span style="color: #F5F752; margin: 0 10px;">✅ 🇷🇺 Русский (current)</span> |
<a href="./README.md">🇺🇸 English</a>

</div>

---

## Установка 🚏

```console
# клонируем репозиторий
$ git clone https://github.com/Louise-h-aa/qrclip.git

# переходим в директорию qrclip
$ cd qrclip

# устанавливаем зависимости
$ python3 -m pip install -r requirements.txt
```

## Использование 🔗

```console
python3 qrclip.py
```

## Автоматизация 📳

> [!IMPORTANT]
> Для автономной работы в `Linux` создайте сервис в папке `etc/systemd/system` с именем [qrclip.service](configs/qrclip.service)

> текст сервиса:

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
> Обратите внимание, что `пользователь` (root), от имени которого запускается сервис, и `директория` (/opt/qrclip) могут быть изменены вами по своему усмотрению
