from PIL import Image

# 定义颜色替换函数
def replace_colors(image_path, new_colors):
    # 加载图像
    img = Image.open(image_path)
    # 转换为 RGBA，如果图像为 RGB
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    data = img.getdata()
    new_data = []

    # 替换颜色
    for item in data:
        # 由于 JPEG 压缩引起的颜色误差，使用近似值
        if item[0] > 150 and item[1] < 100 and item[2] < 100:  # 红色
            new_data.append(new_colors['red'])
        elif item[0] < 100 and item[1] < 100 and item[2] > 150:  # 蓝色
            new_data.append(new_colors['blue'])
        else:
            new_data.append(item)  # 保留原色

    # 更新图像数据
    img.putdata(new_data)
    return img

# 定义新的颜色映射
new_colors = {
    'red': (255, 255, 0, 255),  # 红色变为黄色
    'blue': (0, 255, 0, 255)   # 蓝色变为绿色
}

# 载入并处理每张图片
paths = [
    './part3_0.0001.jpg',
    # './part3_0.001.jpg',
    # './part3_0.0002.jpg',
    './part3_0.0005.jpg'
]

# 替换颜色并显示图像
modified_images = [replace_colors(path, new_colors) for path in paths]
modified_images[0].show()  
modified_images[1].show()
# modified_images[2].show()