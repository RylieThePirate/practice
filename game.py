import random
# def gives a name to a block of code
# can give it parameters
def play_game():
    global keep_playing
    # global uses the variable (keep_playing) outside of the procedure
    secret_number = random.randrange(0, 10)
    number_guesses = 0
    done = False
    # repeats while the condition specified is true
    while not done:
        print "Guess a number between 0 and 10"
        guess = int(raw_input())
        number_guesses = number_guesses + 1
        # number_guesses += 1
        if guess < secret_number:
            print "Too low, billyboy"
        elif guess > secret_number:
            print "Overshot there a bit"
        else:
            print "SWAAAEEET! You got it"
            done = True
            print "Aw heck, you guessed " + str(number_guesses) + " times!"
            print "Would you like to play again?"
            answer = raw_input()
            if answer == "no":
                keep_playing = False
                print "Bye bitch"
keep_playing = True
while keep_playing:
    play_game()
