#!/usr/bin/python3
"""
Main file for testing
"""


validUTF8 = __import__('0-validate_utf8').validUTF8
# 1
data = [65]
print(validUTF8(data))
# 2
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))
# 3
data = [197, 130, 1]
print(validUTF8(data))
# 4
data = [192, 160]
print(validUTF8(data))
# 5
data = [229, 65, 12, 25]
print(validUTF8(data))
# 6
data = [137, 0b11, 0b11, 0b11]
print(validUTF8(data))
