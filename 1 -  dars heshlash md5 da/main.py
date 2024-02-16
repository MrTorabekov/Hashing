import hashlib

print(hashlib.algorithms_available)

matn = "Bitcoin 5"

hash_bit = hashlib.md5(str(matn).encode('utf-8')).hexdigest()

print(hash_bit)