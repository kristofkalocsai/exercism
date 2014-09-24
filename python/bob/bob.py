def hey(sentence):
    if sentence == '':
        return 'Fine. Be that way!'
    if sentence.endswith('?'):
        return 'Sure.'
    if sentence.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
