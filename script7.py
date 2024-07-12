### chap02/script7.py
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
            # Look for an opening double quote
            for i in range(len(the_line)):
                if the_line[i] == '"':
                    # Capture dialogue and transition to S1
                    dialog = the_line[i:]
                    looking_for_open_quote = False
                    break
            
        else:                        # in S1
            # Do other work

print("The End.")
