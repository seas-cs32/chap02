### chap02/script4.py
my_book = input('What book would you like as a script? ')

with open('txts/' + my_book) as my_open_book:
    # Set our FSM to the start state
    looking_for_open_quote = True

    while True:
        the_line = my_open_book.readline()

        # Check for EOF
        if the_line == '':
            break

        # new pseudocode goes here
        if looking_for_open_quote:   # in S0
            # Do some work

            # Part of which is transitioning between states
            if '"' in the_line:
                # move to s1
            else:
                # stay in s0

        else:                        # in S1
            # Do other work

print("The End.")
