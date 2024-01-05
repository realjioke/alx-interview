#!/usr/bin/python3
""" This module validates a stream of utf8 data """
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
        Confirms if a set of data is a valid utf8 encoding
        Returns True if valid or false if not valid
    """

    jump = 0
    n = len(data)
    for i in range(n):
        if jump > 0:
            """ Skip to the next character """
            jump -= 1
            continue

        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10FFFF:
            """ if the character is greater than 1114111 or less than 0 """
            return False
        elif data[i] <= 0x7f:
            """
                If the integer is less than 127, then it is 1 byte long and
                a single character so we wont jump past the next integer
            """
            jump = 0
        elif data[i] & 0b11111000 == 0b11110000:
            """ Check if data[i] is 11110xxx for a 4 byte utf-8 character """
            span = 4
            if n - i >= span:
                """ If there are 3 bytes or more left in the data;
                    check if the next 3 bytes are 10xxxxxx
                """
                if data[i + 1] & 0b11000000 == 0b10000000:
                    if data[i + 2] & 0b11000000 == 0b10000000:
                        if data[i + 3] & 0b11000000 == 0b10000000:
                            jump = span - 1
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            """ Check if data[i] is 1110xxxx for a 3 byte utf-8 character """
            span = 3
            if n - i >= span:
                """
                    If there are 2 bytes or more left in the data;
                    check if the next 2 bytes are 10xxxxxx
                """
                if data[i + 1] & 0b11000000 == 0b10000000:
                    if data[i + 2] & 0b11000000 == 0b10000000:
                        jump = span - 1
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            """ Check if data[i] is 110xxxxx for a 2 byte utf-8 character """
            span = 2
            if n - i >= span:
                """
                    If there is 1 byte or more left in the data;
                    check if the next byte is 10xxxxxx
                """
                if data[i + 1] & 0b11000000 == 0b10000000:
                    jump = span - 1
                else:
                    return False
            else:
                return False
        else:
            return False

    return True
