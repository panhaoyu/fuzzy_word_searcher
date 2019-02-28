import lib.dictionary

dictionary = lib.dictionary.Dictionary()

while True:
    start = input(f'Start: ')
    center = input(f'Center: ')
    end = input(f'End: ')
    result = dictionary.search(
        start=start, center=center, end=end,
        is_phrase=False
    )
    for word, translation in result:
        print(word.rjust(20), end='  ')
        if translation:
            print(translation.replace('\n', '\n' + ''.rjust(22)), end='')
        print()
