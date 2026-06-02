import cv2
import os
import shutil

# 1. Đường dẫn thư mục chuẩn theo máy của bạn
source_folder = "C:/Users/LENOVO/Downloads/palmistry/_train_data"
folder_M = "C:/Users/LENOVO/Downloads/palmistry/_train_data/Tay_Chu_M"
folder_Normal = "C:/Users/LENOVO/Downloads/palmistry/_train_data/Tay_Binh_Thuong"

# Tạo folder nếu chưa có
os.makedirs(folder_M, exist_ok=True)
os.makedirs(folder_Normal, exist_ok=True)

# 2. Quét toàn bộ ảnh thô trong folder gốc
for filename in os.listdir(source_folder):
    # Chỉ xử lý các file là ảnh (bỏ qua các thư mục con)
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(source_folder, filename)
        
        # Đọc và hiển thị ảnh
        img = cv2.imread(img_path)
        
        # Thu nhỏ ảnh lại để không bị tràn màn hình laptop
        img_resized = cv2.resize(img, (600, 600)) 
        
        cv2.imshow("Phan loai - Phim 'm' (Chu M) | Phim 'n' (Binh thuong) | Phim 'q' (Thoat)", img_resized)
        
        # Đợi người dùng bấm phím
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('m'):
            shutil.move(img_path, os.path.join(folder_M, filename))
            print(f"Đã di chuyển: {filename} -> Tay_Chu_M")
        elif key == ord('n'):
            shutil.move(img_path, os.path.join(folder_Normal, filename))
            print(f"Đã di chuyển: {filename} -> Tay_Binh_Thuong")
        elif key == ord('q'):
            print("Đã dừng phân loại!")
            break

cv2.destroyAllWindows()