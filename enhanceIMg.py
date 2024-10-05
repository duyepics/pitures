import cv2
import numpy as np
from matplotlib import pyplot as plt

def create_sharpening_kernel(level):
    """
    Tạo kernel để tăng cường độ nét.
    level: mức độ chi tiết (mức độ cao hơn sẽ tăng cường độ nét nhiều hơn)
    """
    return np.array([[0, -1, 0],
                     [-1, 4 + level, -1],
                     [0, -1, 0]])

def increase_image_quality(image_path, output_path, level=1):
    # Đọc ảnh từ file
    image = cv2.imread(image_path)

    if image is None:
        print("Không thể mở/đọc ảnh. Vui lòng kiểm tra lại đường dẫn.")
        return

    # Tạo kernel để tăng cường độ nét
    kernel = create_sharpening_kernel(level)

    # Áp dụng bộ lọc
    sharpened = cv2.filter2D(image, -1, kernel)

    # Lưu ảnh đã được tăng cường chất lượng
    cv2.imwrite(output_path, sharpened)
    print(f"Ảnh đã được lưu tại {output_path}")

    # Hiển thị ảnh gốc và ảnh đã tăng cường độ nét
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title('Sharpened Image')
    plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))

    plt.show()

    return sharpened

# Đường dẫn tới ảnh cần cải thiện chất lượng
image_path = r"D:\Downloads\724b8.jpg"
output_path = r"D:\Downloads\724b8A.jpg"
level = 1.2  # Bạn có thể thay đổi giá trị này để điều chỉnh mức độ chi tiết

increase_image_quality(image_path, output_path, level)

