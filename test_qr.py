import qrcode
import os
import sys
from datetime import datetime

def test_qr_generation():
    try:
        # 使用时间戳创建目录名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        images_path = os.path.join('images', timestamp)
        
        # 确保目录存在
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        
        # 创建测试二维码
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Test QR Code')
        qr.make(fit=True)

        # 生成图片
        img = qr.make_image(fill_color="black", back_color="white")
        test_file = os.path.join(images_path, 'test_qr.png')
        img.save(test_file)
        
        # 验证文件是否成功创建
        if os.path.exists(test_file):
            print(f"QR code successfully generated at: {test_file}")
        else:
            print("Failed to create QR code file")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    test_qr_generation() 