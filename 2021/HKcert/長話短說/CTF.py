from Crypto.Cipher import AES

master_secret = 68772469292224401385065289104411284170406414625778659512340810023519001149451

master_secret = int.to_bytes(master_secret, 32, "big")
enc = bytes.fromhex("67661f599ae04f576705bd340dc7e014d8c82370b63854654eb4fd6616662cc2bddbb130a90443b735984a2222e9e207e78b20af4fee8b79ada7c2410121fec520e4216aa07e5e7815b670cd1bc57dce")

cipher = AES.new(master_secret, AES.MODE_CBC, b'\0'*16)
flag = cipher.decrypt(enc)
print(flag)

