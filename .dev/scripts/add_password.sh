# Get repo root folder
ROOT_FOLDER=$(git rev-parse --show-toplevel)

RANDOM_TITLE=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)

python main.py --action add_password --email toto@toto.com --title $RANDOM_TITLE --username bob --password 1234 --notes notes --key mysecrectkey
