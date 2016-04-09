import re


def my_strip(str_to_strip, str_to_remove=''):
    remove_regex = re.compile(str_to_remove)
    removed_string = remove_regex.sub(r'', str_to_strip)

    strip_regex = re.compile(r'^\s*(\w.*\w)\s*$')
    match_object = strip_regex.search(removed_string)
    print(match_object.group(1))


my_strip('   haha   test  haha   ', 'test')
my_strip('   haha   test  haha   ')
my_strip('haha   test  haha   ')
my_strip('haha   test  haha')
