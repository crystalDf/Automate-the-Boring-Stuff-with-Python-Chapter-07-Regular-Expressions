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

"""
Remember that the dot character will match just one character
"""
at_regex = re.compile(r'.at')
match_object = at_regex.findall('The cat in the hat sat on the flat mat.')
print(match_object)

"""
You can use the dot-star (.*) to stand in for that “anything.”
Remember that the dot character means
“any single character except the newline,”
and the star character means
“zero or more of the preceding character.”
"""
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match_object = name_regex.search('First Name: Al Last Name: Sweigart')
print(match_object.group(1))
print(match_object.group(2))

nongreedy_regex = re.compile(r'<.*?>')
match_object = nongreedy_regex.search('<To serve man> for dinner.>')
print(match_object.group())

greedy_regex = re.compile(r'<.*>')
match_object = greedy_regex.search('<To serve man> for dinner.>')
print(match_object.group())

no_newline_regex = re.compile('.*')
match_object = no_newline_regex.search('Serve the public trust.\n'
                                       'Protect the innocent. \n'
                                       'Uphold the law.')
print(match_object.group())

newline_regex = re.compile('.*', re.DOTALL)
match_object = newline_regex.search('Serve the public trust.\n'
                                    'Protect the innocent. \n'
                                    'Uphold the law.')
print(match_object.group())

robocop = re.compile(r'robocop', re.I)
match_object = robocop.search('RoboCop is part man, part machine, all cop.')
print(match_object.group())
match_object = robocop.search('ROBOCOP protects the innocent.')
print(match_object.group())
match_object = robocop.search('Al, why does your programming book talk about '
                              'robocop so much?')
print(match_object.group())

"""
The sub() method for Regex objects is passed two arguments.
The first argument is a string to replace any matches.
The second is the string for the regular expression.
The sub() method returns a string with the substitutions applied.
"""
names_regex = re.compile(r'Agent \w+')
match_object = names_regex.sub('CENSORED', 'Agent Alice gave the '
                                           'secret documents to Agent Bob.')
print(match_object)

"""
Sometimes you may need to use the matched text itself as part of
the substitution.
In the first argument to sub(), you can type \1, \2, \3, and so on,
to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
"""
names_regex = re.compile(r'Agent (\w)\w*')
match_object = names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that '
                                          'Agent Eve knew Agent Bob was '
                                          'a double agent.')
print(match_object)
