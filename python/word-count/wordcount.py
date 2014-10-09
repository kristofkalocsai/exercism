# 
#                           __                             __
#  _      ______  _________/ /     _________  __  ______  / /_
# | | /| / / __ \/ ___/ __  /_____/ ___/ __ \/ / / / __ \/ __/
# | |/ |/ / /_/ / /  / /_/ /_____/ /__/ /_/ / /_/ / / / / /_
# |__/|__/\____/_/   \__,_/      \___/\____/\__,_/_/ /_/\__/
#
#
def word_count(sentence):
    s=sentence.split()              #splitting the string on whitespaces
    b=set(s)                        #cast to a set for uniquification(is this a word?)
    d={x:s.count(x) for x in b}     #iterate over the set, counting occurrences in the list
    return d
