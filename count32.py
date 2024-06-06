### chap02/count32.py -- used in ALEs 1-5

# Grab the text blurb to process
import sys
#print("sys.argv =", sys.argv)
if (len(sys.argv) == 1):
    blurb = input('Text: ')
elif (len(sys.argv) == 2):
    input_file = sys.argv[1]
    with open('txts/' + input_file) as my_open_file:
        blurb = my_open_file.read()
else:
    sys.exit("Usage: python3 count32.py [blurb.txt]")

# Count the number of non-blank lines in the blurb
# using the Python string method `split`.
lines = 0
# REPLACE ME with a for-loop
print(lines, "line(s)")

# Count the number of alphabet characters in the blurb
# using the Python string method `isalpha`.
letters = 0
# REPLACE ME with a for-loop
print(letters, "letter(s)")

# Count the number of words in the blurb, where a word
# is any sequence of non-whitespace characters surrounded
# by any amount of whitespace. Please use the Python string
# method `split` and one function on sequences.
words = 0 # REPLACE THE 0 with an expression
print(words, "word(s)")
