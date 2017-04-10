import re


def regex_strip(text, remove=None):

    if remove is not None:
        remove_regex = re.compile(remove)
        text = remove_regex.sub("", text)

    strip_regex = re.compile(r"[\S]+")
    mo = strip_regex.search(text)
    striped_text = mo.group()
    return striped_text


def main():
    text = "  abcdefgh     "
    print(regex_strip(text))
    print(regex_strip(text, "abc"))

if __name__ == "__main__":
    main()