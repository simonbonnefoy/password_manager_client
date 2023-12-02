import click
import pprint
from password_manager_client.password import passwords_queries
from password_manager_client.password.password_generator import PasswordGenerator


@click.group()
def main():
    pass

@main.command()
@click.option("--title", prompt="Enter a title", type=str)
@click.option("--email", prompt="Enter your email", type=str)
@click.option("--username", prompt="Enter your username", type=str)
@click.option("--notes", prompt="Enter a note", type=str)
@click.option( "--password", prompt='Enter password \nIf left empty a random password will be generated', hide_input=True, confirmation_prompt=True)
@click.option( "--key", prompt='Enter protecting passphrase', hide_input=True, confirmation_prompt=True)
def add_password_entry(title, email, username, notes, password,key):
    """
    Add a new password to database.
    @param title: Title of the entry in DB
    @param email: user email
    @param username: user mail
    @param notes: notes relative to the entry
    @param password: password to store. If not provided, a random one will be generated
    @param key: Main key to encrypt password.
    @return: None
    """
    if password == '':
        password_generator = PasswordGenerator()
        password = password_generator.generate_password()

    data = {'title': title,
                'username': username,
                'email': email,
                'password': password,
                'notes': notes}
    ret_code = passwords_queries.add_password(key, data)
    if ret_code == '200':
        print('Entry successfully added to databse')


@main.command()
def get_all_entries():
    """
    Get and print all entries from password db.
    Password are printed encrypted. No decription at this stage
    @return:  None
    """
    entries = passwords_queries.get_passwords()
    pprint.pprint(entries)

@main.command()
@click.option("--password_id", prompt="password id", type=str)
@click.option( "--key", prompt='Enter protecting passphrase', hide_input=True)
def get_password_by_id_to_clipboard(password_id, key):
    """
    Get password by id and store it into the clipboard
    @param password_id: id of password to retrieve
    @param key: Main key use to encrypt password
    @return: None
    """
    passwords_queries.get_password_by_id_to_clipboard(password_id, key)


if __name__ == "__main__":
    main()