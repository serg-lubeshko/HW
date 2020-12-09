from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes


def encrypt(plain_text, password, number):
    if number == 1:
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        content_en, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
        return {
            'content_en': b64encode(content_en).decode('utf-8'),
            'salt1': b64encode(salt).decode('utf-8'),
            'nonce1': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag1': b64encode(tag).decode('utf-8')
        }
    elif number == 2:
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        title_en, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
        return {
            'title_en': b64encode(title_en).decode('utf-8'),
            'salt2': b64encode(salt).decode('utf-8'),
            'nonce2': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag2': b64encode(tag).decode('utf-8')
        }

# def decrypt(enc_dict, password):
#     # decode the dictionary entries from base64
#     salt = b64decode(enc_dict['salt'])
#     content_en = b64decode(enc_dict['content_en'])
#     nonce = b64decode(enc_dict['nonce'])
#     tag = b64decode(enc_dict['tag'])
#
#     # generate the private key from the password and salt
#     private_key = hashlib.scrypt(
#         password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
#
#     # create the cipher config
#     cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
#
#     # decrypt the cipher text
#     decrypted = cipher.decrypt_and_verify(content_en, tag)
#
#     return decrypted


# def main():
#     password = input("Password: ")
#
#     # First let us encrypt secret message
#     encrypted = encrypt("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", password)
#     print(encrypted)
# ---------------------------------------------------------------------------------
# Let us decrypt using our original password
# decrypted = decrypt(encrypted, password)
# print(bytes.decode(decrypted))


# main()
