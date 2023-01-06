### chap02/read32.py
my_book = input('What book would you like to read? ')

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()
        print(the_line, end='')
        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
