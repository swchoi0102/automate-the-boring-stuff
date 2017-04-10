import re


def strong_check(password):
    length_regex = re.compile(r"^\S{8,}$")
    uppercase_regex = re.compile(r"[A-Z]")
    lowercase_regex = re.compile(r"[a-z]")
    digit_regx = re.compile(r"[0-9]")

    if length_regex.search(password) is not None \
            and uppercase_regex.search(password) is not None \
            and lowercase_regex.search(password) is not None \
            and digit_regx.search(password) is not None:
        return True
    else:
        return False


def main():
    password = "Abcdefjg5"
    print(strong_check(password))  # True
    password = "abcedfged6"
    print(strong_check(password))  # False
    password = "12345678"
    print(strong_check(password))  # False


if __name__ == "__main__":
    main()
