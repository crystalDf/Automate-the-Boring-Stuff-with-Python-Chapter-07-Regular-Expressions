import re

"""
You can define your own character class using square brackets.
"""
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('Robo op eats baby food. BABY FOOD.'))

"""
You can also use the caret symbol (^) at the start of a regex to
indicate that a match must occur at the beginning of the searched text.
Likewise, you can put a dollar sign ($) at the end of the regex to
indicate the string must end with this regex pattern.
And you can use the ^ and $ together to
indicate that the entire string must match the regex.
"""
begins_with_hello = re.compile(r'^Hello')
match_object = begins_with_hello.search('Hello world!')
print(match_object.group())
match_object = begins_with_hello.search('He said hello.')
print(match_object)

whole_string_is_num = re.compile(r'^\d+$')
match_object = whole_string_is_num.search('1234567890')
print(match_object.group())
match_object = whole_string_is_num.search('12345xyz67890')
print(match_object)
match_object = whole_string_is_num.search('12  34567890')
print(match_object)
