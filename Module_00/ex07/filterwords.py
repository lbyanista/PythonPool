import string
import sys

def filter_words(s, n):
    words = [w.translate(str.maketrans('', '', string.punctuation))
             for w in s.split()
             if len(w.translate(str.maketrans('', '', string.punctuation))) > n]
    return words

def main():
    if len(sys.argv) != 3:
        print("ERROR")
        return

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        return

    s = sys.argv[1]
    words = filter_words(s, n)
    print(words)

if __name__ == '__main__':
    main()
