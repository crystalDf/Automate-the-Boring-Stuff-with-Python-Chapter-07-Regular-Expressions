import re

length_regex = re.compile(r'\w{8,}')
uppercase_regex = re.compile(r'\w*[A-Z]\w*')
lowercase_regex = re.compile(r'\w*[a-z]\w*')
digit_regex = re.compile(r'\w*[0-9]\w*')

password = ''

while True:
    is_strong_password = True
    password = input('Please enter your password: ')

    if length_regex.search(password) is None:
        print('Your password should be at least eight characters long.')
        is_strong_password = False

    if uppercase_regex.search(password) is None:
        print('Your password should contain at least one uppercase.')
        is_strong_password = False

    if lowercase_regex.search(password) is None:
        print('Your password should contain at least one lowercase.')
        is_strong_password = False

    if digit_regex.search(password) is None:
        print('Your password should contain at least one digit.')
        is_strong_password = False

    if is_strong_password:
        break

print('Your password is ' + password)
