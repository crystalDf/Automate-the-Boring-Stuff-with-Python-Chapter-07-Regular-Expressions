"""
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)
3. Pass the string you want to search into the Regex object’s search() method.
This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual
matched text.
"""

import re

phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
match_object = phone_num_regex.search('My number is 415-555-4242.')

print('Phone number found: ' + match_object.group())

"""
The first set of parentheses in a regex string will be group 1.
The second set will be group 2.
By passing the integer 1 or 2 to the group() match object method,
you can grab different parts of the matched text.
Passing 0 or nothing to the group() method will return the entire matched text.
"""

phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
match_object = phone_num_regex.search('My number is 415-555-4242.')

print(match_object.group(1))
print(match_object.group(2))
print(match_object.group(0))
print(match_object.group())
print(match_object.groups())

"""
multiple-assignment trick
"""
areaCode, mainNumber = match_object.groups()
print(areaCode)
print(mainNumber)

"""
The \( and \) escape characters in the raw string passed to re.compile()
will match actual parenthesis characters.
"""
phone_num_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
match_object = phone_num_regex.search('My phone number is (415) 555-4242.')
print(match_object.group(1))
print(match_object.group(2))

"""
You can think of the ? as saying,
“Match zero or one of the group preceding this question mark.”
"""
phone_num_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match_object = phone_num_regex.search('My number is 415-555-4242')
print(match_object.group())

match_object = phone_num_regex.search('My number is 555-4242')
print(match_object.group())

"""
search() returns a Match object only on the first instance of matching text
"""
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
match_object = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(match_object.group())

"""
findall() will not return a Match object
but a list of strings —
as long as there are no groups in the regular expression
"""
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
match_object = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match_object)


"""
the regular expression being compiled now has groups in parentheses
"""
phone_num_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups

match_object = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match_object)
