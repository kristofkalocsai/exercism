
#     __          __
#    / /_  ____  / /_
#   / __ \/ __ \/ __ \
#  / /_/ / /_/ / /_/ /
# /_.___/\____/_.___/
#
# 
def hey(sentence):
    if sentence.strip() == '':
        return 'Fine. Be that way!'
    if sentence.isupper():
        return 'Whoa, chill out!'
    if sentence.endswith('?'):
        return 'Sure.'
    return 'Whatever.'
