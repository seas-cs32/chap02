### chap02/script1.py
my_book = input('What book would you like as a script? ')

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break

        # new pseudocode goes here