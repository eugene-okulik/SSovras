text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
       ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
new_str = []
for word in text.split():
    if word.endswith('.'):
        word = word[:-1] + 'ing.'
    elif word.endswith(','):
        word = word[:-1] + 'ing,'
    else:
        word = word + 'ing'
    new_str.append(word)
print(' '.join(new_str))
