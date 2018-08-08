
def initBoard(word):
    temp = []
    for i in word:
        temp.append('_')
    return temp

def printBoard(board, guesslist):
    print " ".join(board)
    print "Guesses: " + " ".join(guesslist)

def addGuess(board,word,guess):
    for i in range(len(word)):
        if guess == word[i]:
            board[i] = guess

def game():
    chosenword = "programming".lower()
    guesses = []
    board = initBoard(chosenword)

    while '_' in board:
        printBoard(board,guesses)
        guess =  raw_input('Enter a letter: ').lower()

        if len(guess) == 1:
            if guess in chosenword:
                addGuess(board,chosenword,guess)

            guesses.append(guess)
    else:
        print " ".join(board)
        print "Congrats!! you guessed it correctly"

game()
