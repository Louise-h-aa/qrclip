<h1 align="center">
  qrclip
</h1>

<div align="center">

<strong>语言: </strong>
<span style="color: #F5F752; margin: 0 10px;">✅ CN 中文（当前）</span> |
<a href="./README.ru.md">RU Russian</a> |
<a href="./README.md">US English</a>

</div>

---

## 安装 🚏

```console
# 克隆仓库
$ git clone https://github.com/Louise-h-aa/qrclip.git

# 进入 qrclip 目录
$ cd qrclip

# 安装依赖
$ python3 -m pip install -r requirements.txt
```

## 使用 🔗

```console
python3 qrclip.py
```

## 自动化 📳

> [!IMPORTANT]
> 为了在 `Linux` 上实现自动运行，请在 `etc/systemd/system` 目录中创建服务文件 [qrclip.service](configs/qrclip.service)

> 服务内容：

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
> 请注意，运行服务的 `用户`（root）以及 `目录`（/opt/qrclip）可以根据你的需求自行修改
