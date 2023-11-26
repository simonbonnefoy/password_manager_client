from password_manager_client.cryptography.aes_cipher import AESCipher
import pyperclip
import argparse
import requests
import pprint
import json


def get_arguments() -> argparse.ArgumentParser.parse_args:
    parser = argparse.ArgumentParser(description='Client for password managert')

    parser.add_argument('--key', dest='key', required=False,
                        help='Key to read/write databse')

    parser.add_argument('--action', dest='action', required=True,
                        help='Action to perform ;')

    parser.add_argument('--title', dest='title', required=False,
                        help='Action to perform ;')
    parser.add_argument('--email', dest='email', required=False,
                        help='Action to perform ;')
    parser.add_argument('--username', dest='username', required=False,
                        help='Action to perform ;')
    parser.add_argument('--password', dest='password', required=False,
                        help='Action to perform ;')
    parser.add_argument('--notes', dest='notes', required=False,
                        help='Action to perform ;')

    parser.add_argument('--id', dest='id', required=False,
                        help='Action to perform ;')

    args = parser.parse_args()
    return args

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

def get_password_by_id(id: int, key) -> None:
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

# --action add_password --email toto@toto.com --title test2 --username bob --password 1234 --notes notes --key mysecrectkey
# --action get_passwords
# --action get_password --id id

if __name__ == '__main__':
    args = get_arguments()
    if args.action == 'add_password':
        data = {'title': args.title,
                'username': args.username,
                'email': args.email,
                'password': args.password,
                'notes': args.notes}
        response_code = add_password(args.key, data)
        print(f'response code: {response_code}')
    elif args.action == 'get_passwords':
        responses = get_passwords(args.key)
        for response in responses:
            pprint.pprint(response)
    elif args.action == 'get_password':
        response = get_password_by_id(args.id, args.key)
