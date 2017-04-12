def main():

    with open('input_text') as text:
        input_data = text.read()

    words = input_data.split()
    words_dict = {k: v for k, v in enumerate(words)}
    check_words = ["ADJECTIVE", 'NOUN', 'ADVERB', 'VERB']

    for idx, word in words_dict.items():
        for cw in check_words:
            if cw in word:
                print('Enter an {}:'.format(word.lower()))
                words_dict[idx] = input()

    print(' '.join(words_dict.values()))


if __name__ == '__main__':
    main()