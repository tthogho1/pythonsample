import struct
from PIL import Image

def parse_bmp_header(file_path):
    with open(file_path, 'rb') as f:
        # ファイルヘッダの解析
        file_header = f.read(14)
        (file_type, file_size, _, _, data_offset) = struct.unpack('<2sIHHI', file_header)
        
        print('ファイルタイプ:', file_type.decode())
        print('ファイルサイズ(byte):', file_size)
        print('データオフセット(byte):', data_offset)

        image_header = f.read(40)
        (header_size, width, height, planes, bit_depth, compression, biSizeImage, biXPelsPerMeter, biYPelsPerMeter, ClrUsed, _) \
        = struct.unpack('<IiiHHIIIIII', image_header)
        
        print('ヘッダサイズ(byte):', header_size)
        print('画像幅:', width)
        print('画像高さ:', height)
        print('プレーンの数:', planes)
        print('ピクセルあたりの色数:', bit_depth)
        print('圧縮形式:0で圧縮なし', compression)
        print('ビットマップビットのサイズ:', biSizeImage)
        print('水平解像度:', biXPelsPerMeter)
        print('垂直解像度:', biYPelsPerMeter)
        print('カラーテーブルエントリ数:', ClrUsed)
        
        # RGBQUADの解析
        if bit_depth == 8:
            color_table = f.read(4 * 256)
            print('RGBQUAD:')
            for i in range(256):
                (blue, green, red, _) = struct.unpack('<BBBB', color_table[i*4:(i+1)*4])
                print(f'Color {i}: R={red}, G={green}, B={blue}')



parse_bmp_header('C:\\temp\\test\image\output.bmp')
