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
            valid_utf8 = False
            break

        byte_bin = byte_bin.zfill(8)

        if byte_count == 0:

            continuation_bits = 0

            for i in byte_bin:
                if i == '0':
                    break
                continuation_bits += 1

            byte_count = continuation_bits
            continue

        if byte_count > 0:
            if byte_bin[:2] != '10':
                valid_utf8 = False
                break
            byte_count -= 1
    return valid_utf8
