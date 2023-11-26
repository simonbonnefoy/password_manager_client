# Get repo root folder
ROOT_FOLDER=$(git rev-parse --show-toplevel)

python $ROOT_FOLDER/main.py --action get_passwords --key my_secret_key
