import re

"""
You can define your own character class using square brackets.
"""
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('Robo op eats baby food. BABY FOOD.'))
