import sys

def text_analyzer(text = None):

    """
    This function takes a single argument as string, in case if nothing provided or None it will prompt the user to provide a string.
    Once the string is provided, it will display the sums of its upper-case characters, lower-case characters, punctuation characters and spaces.
    If the argument is not a string, it will print an error message.
    """

    if text is None:
        if len(sys.argv) > 2:
            print("Error: More than one argument provided.")
            return 
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to analyze?\n")
    if not isinstance(text, str):
        print("Error: Argument is not a string.")
        return
    total_count = 0
    upper = 0
    lower = 0
    spaces = 0
    punctuation = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif not char.isalnum():
            punctuation += 1
        total_count += 1

    print(f"The text contains {total_count} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")

if __name__ == "__main__":
    text_analyzer()