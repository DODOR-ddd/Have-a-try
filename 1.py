import base64

# 编码表和数据
STANDARD_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
CUSTOM_TABLE = "ABCDEFGHIJKLMNabcdefghijklmnopqrstuvwxyzOPQRSTUVWXYZ0123456789+/"
ENCODED_STR = "dEFfc1dGq1pxMgMWnihrMx9mewNgdvIWMvctrc"

def custom_base64_decode(encoded_str, custom_table, standard_table):
    trans = str.maketrans(custom_table, standard_table)
    standard_encoded = encoded_str.translate(trans)
    
    padding = 4 - len(standard_encoded) % 4
    if padding != 4:
        standard_encoded += '=' * padding
    
    return base64.b64decode(standard_encoded)

# 解码
try:
    decoded_data = custom_base64_decode(ENCODED_STR, CUSTOM_TABLE, STANDARD_TABLE)
    decoded_str = decoded_data.decode('utf-8')
    print("解码结果:", decoded_str)
except Exception as e:
    print("解码失败:", e)
    print("原始字节:", custom_base64_decode(ENCODED_STR, CUSTOM_TABLE, STANDARD_TABLE))