import re


def my_strip(str_to_strip, str_to_remove=''):
    remove_regex = re.compile(str_to_remove)
    removed_string = remove_regex.sub(r'', str_to_strip)

    print(removed_string)

    # strip_regex = re.compile(r'^\s*(\w*)\s*$')
    strip_regex = re.compile(r'([^\s]*)\s*$')
    match_object = strip_regex.search(removed_string)
    print(match_object.group(1))


my_strip('   haha   test  haha   ', 'test')
