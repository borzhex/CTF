# file: xor_bruteforce.py
# Практическая работа: основы CTF
# Тема: перебор XOR с одним байтовым ключом
# Автор: BORZHEX

def xor_decrypt(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)

def is_printable(data: bytes) -> bool:
    return all(32 <= b <= 126 or b in (10, 13) for b in data)

if __name__ == "__main__":
    ciphertext = bytes.fromhex(
        "1b37373331363f78151b7f2b783431333d78397828372d36"
    )

    for key in range(256):
        plaintext = xor_decrypt(ciphertext, key)
        if is_printable(plaintext):
            print(f"KEY={key:02x} TEXT={plaintext.decode(errors='ignore')}")
