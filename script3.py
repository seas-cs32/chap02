### chap02/script3.py
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
            i = the_line.find('"')
            if i != -1:
                # Found an open quote
                dialog = the_line[i:]
                looking_for_open_quote = False
                # FIXME! Need to handle short dialogue.

        else:                        # in s1
            i = the_line.find('"')
            if i != -1:
                # Found a close quote
                dialog += the_line[:i+1]
                print("\nACTOR:", dialog)
                looking_for_open_quote = True
            else:
                dialog += the_line
            # FIXME! Is this all the work in state S1?
