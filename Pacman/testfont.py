from PIL import Image, ImageOps

# Đường dẫn đến hình ảnh
image_path = 'images/easyMap.png'

# Đọc hình ảnh
image = Image.open(image_path)

# Kích thước của frame
frame_width = 10  # Đặt kích thước frame theo ý muốn
frame_color = 'black'  # Đặt màu của frame theo ý muốn

# Tạo frame
framed_image = ImageOps.expand(image, border=frame_width, fill=frame_color)

# Hiển thị hình ảnh trong frame
framed_image.show()