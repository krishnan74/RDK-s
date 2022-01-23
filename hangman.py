import random
with open("words.txt", "r") as f:
    total_words = f.read()
    words = list(map(str, total_words.split('\n')))

def display():
    global count
    if count == 6:
        print("   _____ \n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif count == 5:
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        print("Wrong guess. " + str(count) + " guesses remaining\n")

    elif count == 4:
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        print("Wrong guess. " + str(count) + " guesses remaining\n")

    elif count == 3:
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /| \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        print("Wrong guess. " + str(count) + " last guess remaining\n")

    elif count == 2:
        print("   _____ \n"
                "  |     | \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        print("Wrong guess. " + str(count) + " last guess remaining\n")
    
    elif count == 1:
        print("   _____ \n"
                "  |     | \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    /  \n"
                "  |      \n"
                "__|__\n")
        print("Wrong guess. " + str(count) + " last guess remaining\n")

    elif count == 0:
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "  |      \n"
                "__|__\n")
        run = False

run = True 
newword = "hangman"
word = newword.upper()
letterlist=[]
count = 6
run = True
while True:
    display()
    guess_letter = input("Enter a letter: ").upper()
    letterlist.append(guess_letter)
    checklist=[]
    for x in word:
        if x in letterlist:
            print(x, end=" ")
            checklist.append(x)
        else:
            print("_", end=" ")
    for x in guess_letter:
        if x not in word:
            count-=1       
    if len(checklist)==len(word):
        run = False
    print(letterlist)
