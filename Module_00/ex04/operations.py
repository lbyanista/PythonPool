import sys


def operations(A, B):
    # if B == 0:
    #     print("Quotient: ERROR (division by zero)")
    #     print("Remainder: ERROR (modulo by zero)")
    # else:
    #     print("Sum: ", A+B)
    #     print("Difference: ", A-B)
    #     print("Product: ", A*B)
    #     print("Quotient: ", A/B)
    #     print("Remainder: ", A%B)
    print("Sum: ", A+B)
    print("Difference: ", A-B)
    print("Product: ", A*B)
    try:
        print("Quotient: ", A/B)
    except:
        print("Quotient: ERROR (division by zero)")
    try:
        print("Remainder: ", A % B)
    except:
        print("Remainder: ERROR (modulo by zero)")


def main():
    if len(sys.argv) == 1:
        print("Usage: python operations.py <number1> <number2>")
        print("Example: python operations.py 12 10")
        sys.exit()

    if len(sys.argv) > 3:
        print("AssertionError: too many arguments")
        sys.exit()

    # assert len(sys.argv) == 3, "This script takes exactly 2 arguments. {} given".format(len(sys.argv) - 1)

    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        operations(A, B)
    except ValueError:
        print("AssertionError: only integers")


if __name__ == "__main__":
    main()
