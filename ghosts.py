# load dictionary /usr/share/dict/words
dictionary = open("/usr/share/dict/words", "r")
contents = dictionary.readlines()
word_list = []
for word in contents:
    if len(word) > 4:
        word_list.append(word.rstrip('\n'))

# ask for the # of players (2)
# while game has not ended:
#   for each player:
#     ask for move
#     if move is "call":
#       if something in the dictionary starts with the word:
#         this player loses
#       else:
#         last player loses
#     if anything in the dictionary is the word + that move:
#       this player loses
keep_playing = True
current_word = ""
while keep_playing:
    for player in range(2):
        print "Player " + str(player + 1) + ", what is your move?"
        move = raw_input()
        current_word = current_word + move
        print current_word
        for word in word_list:
            if word == current_word:
                keep_playing = False
                break
        if not keep_playing:
            break
# things to add:
#   word checking for bluffs
#   valid moves and commands
#   case sensitivity
