# Add your Python code here. E.g.
from microbit import *
import random
import music
from words import wordlist

def newWord():
    print('New game!')
    display.clear()
    global word
    global turn
    word = random.choice(wordlist)
    turn = 0

newWord()

while True:
    print('Turn',turn+1)
    if turn > 4:
        print('You lose. Your score is X/5. The word was ' + word)
        music.play(music.POWER_DOWN)
        sleep(5000)
        newWord()
    guess = input('What is your guess? ')
    if len(guess) != 5:
        print('Not a 5 letter word!')
    else:
        progress = ''
        for a in range(5):
            if guess[a] in word:
                if guess[a] == word[a]:
                    display.set_pixel(a,turn,9)
                    progress = progress + guess[a].upper()
                else:
                    display.set_pixel(a,turn,4)
                    progress = progress + guess[a].lower()
            else:
                progress = progress + '-'
        print(progress)
        turn += 1
        if guess == word:
            print('Congratulations! Your score is ' + str(turn) + '/5')
            music.play(music.POWER_UP)
            sleep(5000)
            newWord()