from gettext import translation


print('Input your english sentence.')
input_msg = input('> ')
words = input_msg.split(' ')

VOWELS = 'aeiou'

word_list = []
pig_list = []

for word in words:
    word_list.append(word)

def translate(word):
    letter_list = []
    core = []
    start = []
    end = 'ay'
    status = False
    
    for x in word:
        letter_list.append(x)

    for x in letter_list:
        if x not in VOWELS:
            if status is False:
                start.append(x)
        else:
            if x in VOWELS:
                status = True
                start_index = letter_list.index(x)
                core.append(letter_list[start_index:])
                break

    core = [val for sublist in core for val in sublist]

    core = ''.join(core)
    start = ''.join(start)

    if str(letter_list[0:]) in VOWELS:
        latin = core + end
    else:
        latin = core + start + end
        
    return latin

for word in word_list:
    pig_list.append(translate(word))

translation = ' '.join(pig_list)
print(translation)