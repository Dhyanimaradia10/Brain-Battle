# Made By: Dhyani Maradia

print("Welcome to the BRAIN BATTLE.....")

print("Rules:--")
print("1. Please ensure that all spellings are correct.")
print("2. Words in any format(Uppercase/Lowercase) will be accepted.")
print("3. Each Question contains 1 mark.")
print("4. There are no negative markings.")
print("If you agree this rules type yes, else type no to quit.")

play = input("Do you want to play: ")

if play.lower() == 'yes':
    print("Okay! Let's Play :) \n")
else:
    quit()

score = 0

#Question 1
question = input("What keyword defines a function? \n")
if question.lower() == 'def':
    print("Correct... \n")
    score+=1
else:
    print("Incorrect... \n")


#Question 2
question = input("How do you start a comment? \n")
if question == '#':
    print("Correct... \n")
    score+=1
else:
    print("Incorrect... \n")


#Question 3
question = input("What data type is True? \n")
if question.lower() == 'boolean':
    print("Correct... \n")
    score+=1
else:
    print("Incorrect... \n")


#Question 4
question = input("How do you import modules? \n")
if question.lower() == 'import':
    print("Correct... \n")
    score+=1
else:
    print("Incorrect... \n")


#Question 5
question = input("Which function gives memory address? \n")
if question.lower() == 'id':
    print("Correct... \n")
    score+=1
else:
    print("Incorrect... \n")


print(f'You got {str(score)} out of 5.')
print(f'You got {str((score/4)*100)}%.')