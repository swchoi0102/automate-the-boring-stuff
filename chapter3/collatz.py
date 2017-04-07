import sys


def main():
    try:
        n = int(input())
    except ValueError:
        print("The input value must be an integer")
    collatz(n)


def collatz(number):
    if number % 2 == 0:
        m = number//2
        print(m)
        if m == 1:
            sys.exit()
        return collatz(m)
    else:
        m = 3*number+1
        print(m)
        if m == 1:
            sys.exit()
        return collatz(m)

if __name__ == "__main__":
    main()