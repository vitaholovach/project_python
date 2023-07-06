import re

def remove_numbers(text_file):
    with open(text_file, 'r+') as file:
        text = file.readlines()
        new_file = re.sub(r'[0-9]+', '', text)
    with open(text_file, 'w') as file:
        file.write(new_file)
