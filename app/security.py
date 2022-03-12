import os

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def generate_key_pair(key_dir: str):
    if not os.path.exists(key_dir):
        os.mkdir(key_dir)

    key = RSA.generate(2048)
    with open(os.path.join(key_dir, 'private.key'), 'wb') as file:
        file.write(key.export_key())

    public_key = key.publickey().export_key()
    return public_key


def check(phrase: bytes, key_dir: str):
    with open(os.path.join(key_dir, 'private.key'), 'rb') as file:
        private_key = RSA.importKey(file.read())

    cipher = PKCS1_v1_5.new(private_key)
    dphrase = ...
