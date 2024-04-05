#!/usr/bin/python3
"""
UTF-8 Code Validation
"""


def validUTF8(data):
    """
    Validate utf-8 code encryption
    """
    valid_utf8 = True

    for val in data:
        if 0 <= val <= 127:
            continue

        val_bin = bin(val)
        val_bin = val_bin[2:]

        if len(val_bin) >= 8:
            val_bin = val_bin.zfill(8)
        else:
            valid_utf8 = False
            continue

        if val_bin[0] == '0' or val_bin[:3] == '110' or \
                val_bin[:4] == '1110' or val_bin[:5] == '11110':
            continue

        valid_utf8 = False
    return valid_utf8
