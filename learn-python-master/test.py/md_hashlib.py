# coding:utf-8
import hashlib
md = hashlib.md5()  # 构造一个md5
md.update('i love here'.encode("utf-8"))
print(md.hexdigest())   # 加密后的字符串
