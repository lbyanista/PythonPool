import sys

def main():
    argc = sys.argv[1:]

    if not argc:
        return
    s = " ".join(argc)

    print(s[::-1].swapcase())
if __name__ == "__main__":
    main()


