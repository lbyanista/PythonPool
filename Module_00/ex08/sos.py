import sys
import string

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    ' ': '/'
}

def morse_decode(s):
    words = s.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(letter)])
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

def main():
    #if more than 2 arguments are passed, merge theme into a single string separated by spaces
    if len(sys.argv) > 1:
        s = ' '.join(sys.argv[1:])
        print(s)
    else:
        #print usage if no argument is passed
        if len(sys.argv) == 1:
            print("Usage: python3 sos.py <string>")
            return
    #convert all letters to uppercase
    s = s.upper()
    print(morse_decode(s))

if __name__ == '__main__':
    main()