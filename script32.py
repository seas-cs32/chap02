### chap02/script32.py
import sys

# Grab the book filename from the command line
if (len(sys.argv) == 2):
    book = sys.argv[1]
else:
    sys.exit("Usage: python3 script32.py book.txt")

with open('txts/' + book) as my_open_book:
    # Set our FSM to the start state
    looking_for_open_quote = True

    while True:
        the_line = my_open_book.readline()

        # Check for EOF
        if the_line == '':
            break

        if looking_for_open_quote:   # in S0
            i = the_line.find('"')
            if i != -1:
                # Found an open quote.  Optimistically grab the
                # rest of the buffer as dialogue.
                dialog = the_line[i:]
                if '"' not in dialog[1:]:
                    # Rest of line was the dialogue.  Transition to S1.
                    looking_for_open_quote = False
                else:
                    # Grab and print the dialogue from this line ...
                    short_dialog = dialog[1:].split('"')[0]
                    print("\nACTOR: " + '"' + short_dialog + '"')
                    # ... and stay in state S0

        else:                        # in S1
            i = the_line.find('"')
            if i != -1:
                # Found a close quote.  Grab the last bit of the line of
                # dialogue we've been collecting, and print it.
                dialog += the_line[:i+1]
                print("\nACTOR:", dialog)
                # Transition to S0.
                looking_for_open_quote = True
            else:
                # No close quote in the line buffer
                dialog += the_line

print("\nThe End.")
