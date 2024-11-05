# Made By: Dhyani Maradia

import random
import time

questions = [
    {
        "question": "What keyword defines a function?",
        "answer": "def",
        "hint": "It's only three letters."
        
    },
    {
        "question": "How do you start a comment?",
        "answer": "#",
        "hint": "It's a single special character."
    },
    {
        "question": "What data type is True?",
        "answer": "boolean",
        "hint": "It represents True or False."
    },
    {
        "question": "How do you import modules?",
        "answer": "import",
        "hint": "Think of bringing something in."
    },
    {
        "question": "Which function gives memory address?",
        "answer": "id",
        "hint": "It's also a term of identity."
    }
]


print("Welcome to the BRAIN BATTLE.....")

print("Rules:--")
print("1. Please ensure that all spellings are correct.")
print("2. Words in any format(Uppercase/Lowercase) will be accepted.")
print("3. You have 10 seconds to answer each question.")
print("4. Each Question contains 1 mark.")
print("5. There are no negative markings.")
print("6. Type hint if you need help with the question.")
print("If you agree this rules type yes, else type no to quit.")

play = input("Do you want to play: ")

if play.lower() == 'yes':
    print("Okay! Let's Play :) \n")
else:
    quit()

score = 0
time_limit = 10   #Setting the time limit of the each question.


#Randomize the questions
random.shuffle(questions)


for i in questions:
    print(i["question"])

    start_time = time.time()

    #  Get the answer
    answer = input().lower()

    elapsed_time=time.time()-start_time
    if elapsed_time>time_limit:
        print("Time's up! Moving to the next question. \n")
        continue

    #Handling the hints
    if answer=='hint':
        print(f'Hint: {i["hint"]}')
        answer = input().lower()
    

    if answer==i["answer"]:
        print("Correct...\n")
        score+=1
    else:
        print(f"Incorrect... The correct answer was '{i["answer"]}'.\n")


print(f'You got {score} out of {len(questions)}.')
percent = (score/len(questions))*100
print(f'You got {percent}%.')
if percent>=30:
    print("Congratulations")
    print("Result: PASS")
else:
    print("Result: FAIL")
    print("Try next time")