# Get repo root folder
ROOT_FOLDER=$(git rev-parse --show-toplevel)

python $ROOT_FOLDER/main.py --action get_password --id 4 --key my_secret_key
