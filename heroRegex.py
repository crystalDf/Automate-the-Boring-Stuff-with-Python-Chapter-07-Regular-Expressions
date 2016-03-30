import re

"""
You can use it anywhere you want to match one of many expressions.
For example, the regular expression r'Batman|Tina Fey' will match
either 'Batman' or 'Tina Fey'.
When both Batman and Tina Fey occur in the searched string,
the first occurrence of matching text will be returned as the Match object.
"""

hero_regex = re.compile(r'Batman|Tina Fey')
match_object = hero_regex.search('Batman and Tina Fey.')
print(match_object.group())

match_object = hero_regex.search('Tina Fey and Batman.')
print(match_object.group())

"""
For example, say you wanted to match any of the strings 'Batman', 'Batmobile',
'Batcopter', and 'Batbat'.
Since all these strings start with Bat, it would be nice if you could specify
that prefix only once. This can be done with parentheses.
"""

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object = bat_regex.search('Batmobile lost a wheel')
print(match_object.group())
print(match_object.group(1))

"""
you want to match only optionally. That is, the regex should find a match
whether or not that bit of text is there.
The ? character flags the group that precedes
it as an optional part of the pattern.
"""

"""
The (wo)? part of the regular expression means that the pattern wo
is an optional group. The regex will match text that has zero instances
or one instance of wo in it.
"""

bat_regex = re.compile(r'Bat(wo)?man')
match_object = bat_regex.search('The Adventures of Batman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())
