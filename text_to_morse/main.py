eng_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '.': '.-.-.-', '?': '..--..', ',': '--..--', ' ': '/'
}

user_entry = input("Write tekst to convert: ")
user_entry = user_entry.split()

morse_word = ''
morse_tekst = ''

for word in user_entry:
    for letter in word:
        if letter not in eng_to_morse:
            print('Data is out of english dictionary!')
        morse_word = morse_word + ' ' + eng_to_morse[letter]
    morse_word = morse_word[1:]
    morse_tekst = morse_tekst + '    ' + morse_word
    morse_word = ''

morse_tekst = morse_tekst[4:]

print(morse_tekst)
