### chap02/script9.py
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
            i = the_line.find('"')
            if i != -1:  # Was the find successful?
                # Found an open quote
                dialog = the_line[i:]
                if '"' not in dialog[1:]:
                    looking_for_open_quote = False
                else:
                    # Grab entire dialog from this line ...
                    short_dialog = dialog[1:].split('"')[0]
                    print("\nACTOR: " + '"' + short_dialog + '"')
                    # ... and stay in state S0

        else:                        # in S1
            i = the_line.find('"')
            if i != -1:  # Was the find successful?
                # Found a close quote
                dialog += the_line[:i+1]
                print("\nACTOR:", dialog)
                looking_for_open_quote = True
            else:
                dialog += the_line
            # FIXME! Is this all the work in state S1?

print("The End.")
