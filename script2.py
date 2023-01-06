### chap02/script2.py
my_book = input('What book would you like as a script? ')

with open('txts/' + my_book) as my_open_book:
    # Set our FSM to the start state
    looking_for_open_quote = True

    while True:
        the_line = my_open_book.readline()

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break

        # new pseudocode goes here
        if looking_for_open_quote:   # in s0
            # do some work; some of it follows
            for i in range(len(the_line)):
                if the_line[i] == '"':
                    dialog = the_line[i:]
                    break

            if '"' in the_line:
                looking_for_open_quote = False

        else:                        # in s1
            # do other work
