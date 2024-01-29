import base64
from Crypto.Util.number import bytes_to_long

# ====
# HAXOR RULEZ
#
# This is NSA level stuff
# ====

FLAG = input("Message: ")

def encode(message):

    return hex(bytes_to_long(base64.b64encode(str.encode(message))))

print(encode(FLAG))