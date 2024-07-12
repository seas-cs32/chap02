### chap02/script1.py
my_book = input('What book would you like as a script? ')

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Check for EOF
        if the_line == '':
            break

        # new pseudocode goes here

print("The End.")
