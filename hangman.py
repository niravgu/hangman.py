import random
words = ["star","fast","poor","dash","wins"]
name = input("hey, what's your name?")
print("hey",name,"now i will think of a word and you have to guess it.")
compselect = random.choice(words)
print("guess a character")
guesses = ''
x = 10
while x>0:
    failed =0
    for a in compselect:
        if a in guesses:
            print(a)
        else :
            print("_")
            failed += 1
    if failed == 0:
        print("hah! you beat me")
        print("the word was",compselect)
        break
    guess =  input("any alphabet please")
    guesses += guess
    if guess not in compselect:
        x -= 1
        print("sorry friend")
        print ("you have",x,"turns left")
        if x ==0:
            print("haha I won")
            print("the word was",compselect)