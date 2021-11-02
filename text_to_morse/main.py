eng_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '.': '.-.-.-', '?': '..--..', ',': '--..--', ' ': '/'
}

user_entry = input("Write tekst to convert: ")
morse_tekst = ''

for letter in user_entry:
    if letter not in eng_to_morse:
        morse_tekst = ' Data is out of english dictionary!'
        break
    elif letter != ' ':
        morse_tekst = morse_tekst + ' ' + eng_to_morse[letter]
    else:
        morse_tekst = morse_tekst + '  '

morse_tekst = morse_tekst[1:]

print(morse_tekst)
