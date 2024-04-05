#!/usr/bin/python3
"""
UTF-8 Code Validation
"""


def validUTF8(data):
    """
    Validate utf-8 code encryption
    """
    valid_utf8 = True
    byte_count = 0

    for byte in data:
        byte_bin = bin(byte)[2:]

        if len(byte_bin) > 8:
            return False

        byte_bin = byte_bin.zfill(8)

        if byte_count == 0:
            continuation_bits = 0

            for i in byte_bin:
                if i == '0':
                    break
                continuation_bits += 1

            if continuation_bits == 0:
                continue 
            elif continuation_bits == 1:
                return False

            byte_count = continuation_bits - 1
            continue

        if byte_count > 0:
            if byte_bin[:2] != '10':
                return False
            byte_count -= 1
    return valid_utf8
