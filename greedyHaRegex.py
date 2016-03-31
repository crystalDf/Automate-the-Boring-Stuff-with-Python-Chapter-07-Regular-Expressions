import re

"""
Python’s regular expressions are greedy by default,
which means that in ambiguous situations
they will match the longest string possible.
"""
greedy_ha_hegex = re.compile(r'(Ha){3,5}')
match_object = greedy_ha_hegex.search('HaHaHaHaHa')
print(match_object.group())

"""
The nongreedy version of the curly brackets,
which matches the shortest string possible,
has the closing curly bracket followed by a question mark.
"""
"""
Note that the question mark can have two meanings in regular expressions:
declaring a nongreedy match or flagging an optional group.
"""
greedy_ha_hegex = re.compile(r'(Ha){3,5}?')
match_object = greedy_ha_hegex.search('HaHaHaHaHa')
print(match_object.group())
