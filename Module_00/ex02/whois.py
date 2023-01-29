import sys


def check_if_number(num):
    if not isinstance(num, int):
        print("AssertionError: argument is not an integer")
        sys.exit()
    if(num == 0):
        print("I'm Zero.")
    if(num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    

def main():
    # argc = sys.argv

    # if not argc:
    #     return
    # s = " ".join(argc)

    if len(sys.argv) != 2:
        print("AssertionError: more than one argument are provided")
        sys.exit()
    else:
        check_if_number(int((sys.argv[1])))
        

if __name__ == "__main__":
    main()