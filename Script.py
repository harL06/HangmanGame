import random

# importing text
words = []
f = open("words.txt", "r", encoding="utf8")
for line in f:
    words.append(line.strip("\n"))


# the hanging men
people= {
  0: ["  P----v  ",
      "  |    0  ",
      "  |   /|\ ",
      "  |   / \ ",
      " -------- "],
1: ["  P----v  ",
      "  |    0  ",
      "  |   /|\ ",
      "  |   /   ",
      " -------- "],
2: ["  P----v  ",
      "  |    0  ",
      "  |   /|\ ",
      "  |       ",
      " -------- "],
3: ["  P----v  ",
      "  |    0  ",
      "  |   /|  ",
      "  |       ",
      " -------- "],
4: ["  P----v  ",
      "  |    0  ",
      "  |    |  ",
      "  |       ",
      " -------- "],
5: ["  P----v  ",
      "  |    0  ",
      "  |       ",
      "  |       ",
      " -------- "],
6: ["  P----v  ",
      "  |       ",
      "  |       ",
      "  |       ",
      " -------- "]
    }


# Checks for legitimate guess
def guess():
    
    currentGuess = str(input("\nPlease enter a letter:\n> ")).lower()
    if len(currentGuess) > 1 or currentGuess not in alphabet:
        print(currentGuess, "isn't a single letter, try again!\n")
        guess()
    elif currentGuess in usedLetters:
        print(currentGuess, "was already guessed, try again!\n")
        guess()
    else:
        usedLetters.append(currentGuess)
        return(currentGuess)

# tracks correct letters and prints updated line
def progress():
    prog = []
    left = 0 #tracks letters left to be guessed
    for letter in word:
        if letter in usedLetters:
            prog.append(letter)
        else:
            prog.append("_")
            left += 1
    print(" ".join(prog), "\n\nLetters remaining:", left)
    print("Guesses remaining:", remGuess)
    return(left)

word = words[random.randint(0, (len(words)-1))]


word = list(word)


# alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# no. guesses remaining
remGuess = 6
usedLetters = []
print("Welcome to hangman!\n")
while remGuess > 0:
    # hanging man code

    man = "\n".join(people[remGuess])
    print(man, "\nWord:")
    
    
    left = progress()
    if left == 0:
        print("You Win!\n")
        break
    print("\nLetters used: ", " ".join(usedLetters))
    currentGuess = guess()
    if currentGuess not in word:
        remGuess -= 1
if remGuess == 0:
    print("Out of guesses, you lose ):")
    man = "\n".join(people[remGuess])
    print(man)
print("The word was:", "".join(word))
