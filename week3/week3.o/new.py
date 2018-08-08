
def initBoard(word):
    temp = []
    for i in word:
        temp.append('_')
    return temp

def printBoard(board, guesslist):
    print " ".join(board)
    print "guesses: " + " ".join(guesslist)

def addGuess(board,word,guess):
    for i in range(len(chosenword)):
        if guess == chosenword[i]:
            board[i] == guess

def games():
    chosenword = "programming".lower()
    guesses = []
    board = initBoard(chosenword).lower()

    while '_' in board:
        printBoard(board,guesses)
        guess =  raw_input('Enter a letter: ').lower()

        if len(guess) == 1:
            if guess in chosenword:
                addGuess(board,chosenword,guess)

            guesses.append(guess)

games()
