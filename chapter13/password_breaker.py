import PyPDF2


def breaker(fname):
    with open('dictionary.txt', 'r') as f:
        dictionary = f.readlines()

    with open(fname, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        for word in dictionary:
            if pdf_reader.decrypt(word) == 1:
                print("The password is {}".format(word))
                break


def main():
    fname = "encrypted.pdf"
    breaker(fname)


if __name__ == "__main__":
    main()