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
        valid_val = val & 0x7F

        if valid_val != val:
            valid_utf8 = False
    return valid_utf8
