### chap02/script6.py
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

            # Part of which is capturing dialogue
            for i in range(len(the_line)):
                if the_line[i] == '"':
                    dialog = the_line[i:]
                    break

            # Part of which is transitioning between states
            if '"' in the_line:
                looking_for_open_quote = False

        else:                        # in S1
            # Do other work

print("The End.")
