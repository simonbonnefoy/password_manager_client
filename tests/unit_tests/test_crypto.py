import pytest
from pytest import fixture
from password_manager_client.cryptography.aes_cipher import AESCipher

@fixture()
def prepare_aes_ciper_object():
    aes_cipher = AESCipher('my_secret_key')
    yield aes_cipher

def test_encrypt_decrypt_str(prepare_aes_ciper_object):
    aes_cipher = prepare_aes_ciper_object
    to_encrypt = 'hello world!'
    encrypted = aes_cipher.encrypt(to_encrypt)
    decrypted = aes_cipher.decrypt(encrypted)
    assert decrypted == to_encrypt
