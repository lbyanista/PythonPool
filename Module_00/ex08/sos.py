import sys

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

def encode_morse(text):
    encoded_text = []
    for c in text.upper():
        if c in morse_code:
            encoded_text.append(morse_code[c])
    return  ' '.join(encoded_text)

def main():
    if len(sys.argv) == 1:
        print("Usage: python sos.py <text>")
    else:
        text = ' '.join(sys.argv[1:])
        print(encode_morse(text))

if __name__ == '__main__':
    main()