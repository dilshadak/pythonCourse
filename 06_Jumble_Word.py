# Python program for jumbled words game.
 
# import random module
import random
from wordlist import words
 
# function for choosing random word.
def choose():
    '''choice() method randomly choose any word from the list.'''

    pick = random.choice(words)
    return pick

# Function for shuffling the characters of the chosen word.
def jumble(word):
    '''sample() method shuffling the characters of the word'''

    random_word = random.sample(word, len(word))
 
    # join() method join the elements of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled

# Function for playing the game.
def play():

    rules = '''
    1. Jumbled word is English workd with jumbled alphabets
    2. Correct the spelling and press Enter
    3. On worng spelling you loose the game
    4. Press 0 to quit the game in between
    '''
    print(rules)
    score = 0
    # keep looping
    while True:
 
        # choose() function calling

        picked_word = choose()
 
        # jumble() function calling
        jumble_word = jumble(picked_word)
        print("jumbled word is :", jumble_word)
        ans = input("what is in your mind? ")

        # checking ans is equal to picked_word or not
        if ans == picked_word:
            score += 1
            print('Your score is :', score)
        else:
            print(f"Sorry you Loose, correct spelling is: {picked_word}")
            break
        c = int(input("press 1 to continue and 0 to quit :"))

        # checking the c is equal to 0 or not
        # if c is equal to 0 then break out
        # of the while loop o/w keep looping.
        if c == 0:
            print('Thank you !!')
            break
# Driver code
if __name__ == '__main__':
    # play() function calling
    play()