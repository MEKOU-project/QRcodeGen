import qrcode

# 1. 変換したいリンク（アンケートURLやPortalのURL）
data = "https://docs.google.com/forms/d/e/1FAIpQLSfbyoYGQlH2Ghf8kqhf5qOW4UsnmUXMk94MLP6xJPR5fBoxJQ/viewform?usp=dialog"

# 2. QRコードの生成
img = qrcode.make(data)

# 3. 保存
img.save("mekou_portal_qr.png")
#pip install qrcode[pil]
