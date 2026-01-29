# file: base_and_rot.py
# Практическая работа: основы CTF
# Тема: Base64 и ROT13
# Автор: BORZHEX

import base64
import codecs

def decode_base64(data: str) -> str:
    return base64.b64decode(data).decode("utf-8", errors="ignore")

def decode_rot13(data: str) -> str:
    return codecs.decode(data, "rot_13")

if __name__ == "__main__":
    encoded_base64 = "ZmxhZ3tleGFtcGxlX2N0Zn0="
    encoded_rot13 = "synt{rknzcyr_pgs}"

    print(decode_base64(encoded_base64))
    print(decode_rot13(encoded_rot13))
