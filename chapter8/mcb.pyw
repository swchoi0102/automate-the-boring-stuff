# ! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage : py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#         py.exe mcb.pyw list - Loads all keywords to clipboard
#         py.exe mcb.pyw delete <keyword> - Delete keyword from the shelf
#         py.exe mcb.pyw delete <- Delete all keywords from the shelf

import shelve
import pyperclip
import sys


def main():

    with shelve.open('mcb') as mcb_shelf:

        if len(sys.argv) == 3:
            if sys.argv[1].lower() == 'save':
                mcb_shelf[sys.argv[2]] = pyperclip.paste()
            elif sys.argv[1].lower() == 'delete':
                del mcb_shelf[sys.argv[2]]

        elif len(sys.argv) == 2:
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(str(list(mcb_shelf.keys())))
            elif sys.argv[1] in mcb_shelf:
                pyperclip.copy(mcb_shelf[sys.argv[1]])
            elif sys.argv[1].lower() == "delete":
                for key in mcb_shelf.keys():
                    del mcb_shelf[key]


if __name__ == "__main__":
    main()