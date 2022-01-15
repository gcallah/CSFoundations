
"""
This program outputs a "table" mapping binary numbers to
their int counterpart.
"""

LAST_CONV = 64

for i in range(LAST_CONV):
    print(f"DEC: {i}: BIN: {bin(i)}")
