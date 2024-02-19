print("".join(chr(((ord(c) - 65 + 13) % 26) + 65) if c.isupper() else chr(((ord(c) - 97 + 13) % 26) + 97) if c.islower() else c for c in input()))
