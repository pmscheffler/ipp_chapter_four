"""Decrypt a path through a Union Route Cipher

Designed for whole-word transposition ciphers with vairable rows & columns
Assumes encryption began at either top or bottom of a column
Key inidicates the order to read columns and the direction to traverse
Negative column numbers mean start at the bottom and read up.
Positive column numbers mean start to the top and read down.

Exmaple belw is for a 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.



Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext..
"""
import sys

#===================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple quotes):
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19
"""

# numer of columns in the transposition matrix:
COLS = 4

# number of rows in the transformation matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex = -1)
key = """ -1 2 -3 4 """

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#====================================================

