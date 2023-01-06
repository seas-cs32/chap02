## CS32 PSet #2

*NOTE: The ["PSet #2" assignment page on the CS 32 Canvas
site](https://canvas.harvard.edu/courses/112459/assignments/644303) indicates when this assignment is due, what materials you should
submit, and how to submit them.*

As promised in the active learning exercises at the end of Chapter 2, this
programming problem set will finish the problem we started in that chapter.

### **Part 1. Chatty characters.**

The first thing you're going to do is write code that cleans up some of the
punctuation used in a story's dialogue that isn't appropriate for a theatrical
script. In particular, this part will have you handle a punctuation oddity in
long pieces of dialogue, i.e., those that span multiple paragraphs.

In literature, dialogue that has a character say two or more paragraphs of
material is formatted such that each paragraph starts with a double-quote
character, but elides the double-quote character from all but the last
paragraph. Here's an example from *The Talkative Tortoise* (see
`txts/Talkative4.txt`):

> And saying, "Truly, O king! those who are called
> chatter-boxes--people whose words have no end--come to grief like
> this," he uttered these Verses:
> 
> "Verily the tortoise killed himself
> Whilst uttering his voice;
> Though he was holding tight the stick,
> By a word himself he slew.
> 
> "Behold him then, O excellent by strength!
> And speak wise words, not out of season.
> You see how, by his talking overmuch,
> The tortoise fell into this wretched plight!"

Your task is to modify `script32.py` so that it **puts back the elided ending
double-quote characters**. Your script's output should look like this:

> ACTOR: "Truly, O king! those who are called
> chatter-boxes--people whose words have no end--come to grief like
> this,"
> 
> ACTOR: "Verily the tortoise killed himself
> Whilst uttering his voice;
> Though he was holding tight the stick,
> By a word himself he slew."
> 
> ACTOR: "Behold him then, O excellent by strength!
> And speak wise words, not out of season.
> You see how, by his talking overmuch,
> The tortoise fell into this wretched plight!"

You can do this by adding one `elif` compound statement to the script.

**HINT**: Which state are you in when this situation occurs? What input event
corresponds to this situation? What do you want your FSM to do on this event and
to where should it transition? In other words, are you *extending the
functionality of an existing state* in our FSM (and adding a new transition), or
are you adding a new state to our FSM?

When you have completed this part, your new version of `script32.py` should
correctly handle our first four tests: `Talkative1.txt`, `Talkative2.txt`,
`HomeView3.txt`, and `Talkative4.txt`.

### **Part 2. Commas to periods.**

If you look closely at your script's output on `Talkative4.txt`, you will notice
that the first line of dialogue ends in a comma. This makes sense in the story,
but not in our output script. Your new task is to **replace any comma you find
at the end of a line dialogue with a period**.

Using `Talkative4.txt` as the test input, go ahead and figure out how to solve
this challenge for the `print` in `script32.py` that actually prints the line of
dialogue with the ending comma.

But that's not the only `print` statement that has to get fixed (i.e.,
`Talkative4.txt` and `HomeView5.txt` exercise different parts of our script). To
fully complete this part, you should create a function called `print_dialog`
that takes a piece of `dialog` (i.e., dialogue from the story enclosed in double
quotes) and prints out that `dialog`. Specifically,
`print_dialog` will perform any cleanup--like converting an ending comma into an
ending period--and decorate the line of dialogue with whatever else we expect
every printed line of dialogue to have.

Here's an example call to `print_dialog` when run in the interactive Python
interpreter:

```python
> print_dialog("I know some good games we could play,")

ACTOR: "I know some good games we could play."
>
```

Please don't forget to prepend a carriage-return character to the front of the
printed line!

When you have completed this part, your new version of `script32.py` should
correctly handle our first five tests: `Talkative1.txt`, `Talkative2.txt`,
`HomeView3.txt`, `Talkative4.txt`, and `HomeView5.txt`.

### **Part 3. Covering any number of double quotes on a file line.**

One of the active learning exercises at the end of Chapter 2 demonstrated that
the final script in that chapter had only solved our problem for file lines with
two or fewer double-quote characters in them. To solve the general problem of
extracting dialogue from a story when processing the story a file line at a
time, we will take advantage of this repeating pattern: A story consists of
narrative prose followed by a piece of dialogue, and then more narrative, which
might be just a piece of whitespace, followed by another piece of dialogue, and
so forth.

If we call `split` on a file line, where double-quote character is the input to
Python's string `split` method, we can create a worklist composed of alternating
strings of narrative and dialogue (or dialogue and narrative). We might then
loop over the elements of this worklist performing an appropriate action for
each element.

Write some pseudocode for processing such a worklist, and then think about where
such a processing loop might have to appear in `script32.py`. Finally, generate
the appropriate worklist at each of your identified points and insert the
processing loop there. In this manner, your script will correctly handle a story
with *any number* of double-quote characters on a file line.

In other words, your script should continue to read from the input file one line
at a time. When it can process the entire file line in one fell swoop, it
should. When it finds one or more double-quote characters, it should do all the
processing it needs to do to handle all the dialogue on the line before reading
the next file line.

You should use `HomeView6.txt`, which contains a line with three double-quote
characters, and `HomeView7.txt`, which contains a line with four double-quote
characters, to test your script. If you think you've added all the code you
need, make sure that your script correctly handles `Talkative8.txt`, as well as
our earlier five text inputs.

### **Part 4. Don't forget to capitalize!**

You probably noticed that `script32.py` when run on `HomeView6.txt` still has a
formatting problem. Here's the output:

```python
~/pset2$ python3 script32.py HomeView6.txt

ACTOR: "Poor things!"

ACTOR: "they haven't had any bringing
up; they've just scrambled up!"

ACTOR: "I must get schooling for
them some way, but I don't see how!"

The End.
~/pset2$ 
```

Yea, the second piece of dialogue starts without a capital letter, which is how
the script found it in the input file.

Because we encapsulated the printing of a line of `dialog` in a procedure, it is
easy to make a single fix in this procedure and have it handle every location in
our script where we print dialogue. Inside this function, figure out what you
need to do to make sure that every piece of `dialog` starts with a capital
letter. **HINT:** There's a string method that can help!

When you have completed this part, your FINAL version of `script32.py` should
correctly all eight of our test inputs: `Talkative1.txt`, `Talkative2.txt`,
`HomeView3.txt`, `Talkative4.txt`, `HomeView5.txt`, `HomeView6.txt`,
`HomeView7.txt`, and `Talkative8.txt`.

Plus, and this is exciting, your script handles the complete text of the Indian
fairy tale *The Talkative Tortoise* (in `Talkative.txt`) and the complete first
chapter in *Five Little Peppers* by Margaret Sidney (in `HomeView.txt`). Try
them! Congratulations on your excellent work!