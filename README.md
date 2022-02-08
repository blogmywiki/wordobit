# wordobit

A micro:bit Python version of a popular word guessing game.

## How to load it
The simplest way is to download the HEX file and drag and drop it onto a micro:bit.
You can also drag and drop the HEX file onto the Python editor https://python.microbit.org/v/alpha
Then click 'connect', flash the program and open the serial console.
The program consists of two files:
- main.py is the main program
- word.py comtains the word list in a separate file (to make it a bit harder to cheat). You can add as many words as you like to this list.


## How to play
You get 5 turns.
Type your guess in on your computer keyboard.
Each row on the micro:bit's LED display shows:
- a bright light for a correct letter in the correct place
- a dim light for letters that are right but in the wrong place
- no light at all if it's the letter isn't in the word.

The console also prints out your progress like this:
--a-T
Lower case letters are in the wrong place.
So 'a' is in the word but in the wrong place.
Upper case letters are in the right place, so this word ends in 'T'.

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
