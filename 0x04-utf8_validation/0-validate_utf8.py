#!/usr/bin/python3
"""
UTF-8 Code Validation
"""


def validUTF8(data):
    """
    Validate utf-8 code encryption
    """
    byte_count = 0

    for byte in data:
        byte_bin = bin(byte)[2:].zfill(8)

        if byte_count == 0:
            continuation_bits = 0

            for i in byte_bin:
                if i == '0':
                    break
                continuation_bits += 1

            if continuation_bits == 0:
                continue
            elif continuation_bits == 1 or continuation_bits > 4:
                return False

            if continuation_bits > 1 and byte_bin[1] == '0':
                return False

            byte_count = continuation_bits - 1
            continue
        else:
            if byte_bin[:2] != '10':
                return False
            byte_count -= 1
    return byte_count == 0
