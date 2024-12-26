import os
import shutil
from PIL import Image

# 设置目标文件夹路径和目标输出文件夹路径
source_folder_path = "/home/dyw/gaussian-splatting/data/mipnerf/treehill/images_4"  # 修改为你的目标文件夹路径
output_folder_path = "/home/dyw/gaussian-splatting/selected_data/mipnerf/treehill"  # 修改为你要保存图片的目标文件夹路径

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(source_folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

# 如果目标文件夹中没有图片，输出提示信息
if not image_files:
    print("目标文件夹中没有图片文件。")
else:
    # 每隔8个文件选取一个（从索引0开始）
    sampled_images = image_files[::8]  # 通过切片操作实现每隔8个取1个
    
    # 打印选中的图片文件
    print(f"选中的图片有：")
    for img_name in sampled_images:
        print(img_name)
    
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # 将选中的图片复制到目标文件夹
    for img_name in sampled_images:
        source_image_path = os.path.join(source_folder_path, img_name)
        output_image_path = os.path.join(output_folder_path, img_name)
        
        # 使用shutil.copy2来复制文件，保留文件的元数据（如修改时间）
        shutil.copy2(source_image_path, output_image_path)
        
        print(f"图片 {img_name} 已复制到 {output_folder_path}")