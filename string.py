"""
import string

abc = string.ascii_lowercase
s = "hello"
key = 5
cypher = s.translate(string.maketrans(abc, abc[key:] + abc[:key]))
print(cypher)
"""


