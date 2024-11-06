import NTRU2

NTRU2.generate_keys("test", mode="moderate")
enc = NTRU2.encrypt("test", "john trixie")
dec = NTRU2.decrypt("test", enc)
print("Decrypted message:", dec)