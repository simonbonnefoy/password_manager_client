from password_manager_client.cryptography.aes_cipher import AESCipher
import pyperclip
import requests
import json
def add_password(key: str, data: dict) -> str:
    """
    Add a password to DB. Password is ciphered before being posted
    @param key: Main key to cipher/decipher password from/to database
    @param data: dictionnary containings entries to store in DB
    @return: status code of post request
    """
    aes_cipher = AESCipher(key)
    data['password'] = aes_cipher.encrypt(data['password']).decode()
    headers = {'accept':'application/json','Content-Type':'application/json'}
    response = requests.post('http://0.0.0.0:8000/passwords/', json=data, headers=headers)
    return response.status_code


def get_passwords() -> requests.Response:
    """
    Get all entries from DB. Password are note decrypted
    @return: json containing all db entries
    """
    response = requests.get('http://0.0.0.0:8000/passwords/?skip=0&limit=100')
    return json.loads(response.text)

def get_password_by_id_to_clipboard(id: int, key) -> None:
    """
    Get password from its id. Password is decrypted and copied to clipboard
    @param id: id of password to retrieve
    @param key: Main key to cipher/decipher password from/to database
    @return: None
    """
    response = requests.get(f'http://0.0.0.0:8000/passwords/ids/{id}')
    response = json.loads(response.text)
    aes_cipher = AESCipher(key)
    password = aes_cipher.decrypt(response['password'].encode())
    pyperclip.copy(password)
    print('password copied to clipboard!')
