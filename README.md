# wordobit

A micro:bit Python version of a popular word guessing game.

## How to load it
You need a browser like Chrome or Edge that supports WebUSB and you'll need to use a Python editor that has a serial console like the main or alpha micro:bit online Python editors.

The simplest way is to download the HEX file and drag and drop it onto a micro:bit.

You can also drag and drop the HEX file onto the Python editor https://python.microbit.org/v/alpha

Then click 'connect', flash the program and open the serial console ('show serial').

The program consists of two files:
- main.py is the main program
- word.py contains the word list in a separate file (to make it a bit harder to cheat). You can add as many words as you like to this list.
You could also load main.py and then word.py in the Python editor and then flash them to a micro:bit.


## How to play
You get 5 turns. The program picks a word at random from the word list. You can add more of your own words to words.py
Type your guess in on your computer keyboard.
Each row on the micro:bit's LED display shows:
- a bright light for a correct letter in the correct place
- a dim light for letters that are right but in the wrong place
- no light at all if it's the letter isn't in the word.

The console also prints out your progress like this:

`--a-T`

Lower case letters are in the word but in the wrong place.

So 'a' is in the word but it's in the wrong place.

Upper case letters are in the right place, so we know this word ends in 'T'.

If you run out of guesses, it tells you what the word was.

If you get it right, it gives you your score.

In either case after a short pause it picks a new word for you.

There's a video about the program and how it works: https://youtu.be/YSkGlyjsL-8

## What is it good for?
You could use this to teach:
- Some Python
- Using the BBC micro:bit
- Using procedures / functions
- Scope of variables in functions
- Parsing strings

You could also easily extend this by adding some simple encryption like ROT-13 to the word list to make it harder to cheat.

![Screenshot from video](/images/screenshot.png)
