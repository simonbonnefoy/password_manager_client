import click
import pprint
from password_manager_client.password import passwords_queries
from password_manager_client.password.password_generator import PasswordGenerator


@click.group()
def main():
    pass


@main.command()
@click.option("--title", prompt=" Enter a title", type=str)
@click.option("--email", prompt=" Enter your email", type=str)
@click.option("--username", prompt=" Enter your username", type=str)
@click.option("--notes", prompt=" Enter a note", type=str)
@click.option("--password", default='', prompt=" Enter a password (if not set a password will be generated for you)", type=str)
@click.option("--key", prompt="key", type=str)
def add_password_entry(title, email, username, notes, password,key):
    if password == '':
        password = PasswordGenerator.generate_password()

    data = {'title': title,
                'username': username,
                'email': email,
                'password': password,
                'notes': notes}
    ret_code = passwords_queries.add_password(key, data)
    print(ret_code)


@main.command()
def get_all_entries():
    entries = passwords_queries.get_passwords()
    pprint.pprint(entries)

@main.command()
@click.option("--password_id", prompt="password id", type=str)
@click.option("--key", prompt="key", type=str)
def get_password_by_id(password_id, key):
    passwords_queries.get_password_by_id(password_id, key)


if __name__ == "__main__":
    main()