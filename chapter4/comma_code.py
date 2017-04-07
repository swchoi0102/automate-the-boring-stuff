def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))


def comma_code(input):
    return ", ".join(input[:-1] + ["and"]) + " cats"


if __name__ == "__main__":
    main()