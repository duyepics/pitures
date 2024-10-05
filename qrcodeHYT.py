import qrcode
import os

# Nhập văn bản từ người dùng
text = input("Nhập văn bản tiếng Việt cần chuyển đổi thành QR code: ")

# Tạo QR code
qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)

# Thêm dữ liệu vào QR code
qr.add_data(text)
qr.make(fit=True)

# Tạo hình ảnh QR code
img = qr.make_image(fill_color="black", back_color="white")

save_directory = "D:\Downloads"
os.makedirs(save_directory, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại

# Lưu hình ảnh QR code
img.save(os.path.join(save_directory, "CodeNo1.png"))

print(f"QR code đã được tạo và lưu thành công trong thư mục {save_directory}!")

