import time
print("--------------------------------------------------")
#Welcome the user
print("Welcome to the ***Sport Quiz Games***!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 2 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) WHO IS THE LEGEND MEN SINGLE BADMINTON IN MALAYSIA?\n(A) Lee Chong Wei \n(B) Mokthar Dahari \n(C) Chia Soon Kit \n(D) Zainal Abidin\n\n")
answer_1= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)HOW MANY PLAYER SEPAK TAKRAW IN REGU?\n(A) One\n(B) Two\n(C) Three\n(D) Four\n\n")  
answer_2 = "c"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  WHO THE MOST SUCCESSFUL SQUASH PLAYER?\n(A) Shazlin Zulkiflee \n(B) Nurul Huda\n(C) Pearly Tan\n(D) Nicol David\n\n")
answer_3= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n") 
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  HOW MANY PLAYER IN FOOTBALL TEAM?\n(A) 11\n(B) 12\n(C) 10\n(D) 9\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5) MOKTHAR DAHARI IS THE LEGEND PERSON IN?\n(A) Sepak Takraw\n(B) Football\n(C) Badminton\n(D) Tennis\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

#question 6
print("==================================================")
question_6 =print("5) HOW MANY PLAYER IN NETBALL TEAM?\n(A) 6\n(B) 7\n(C) 8\n(D) 9\n\n")
answer_6= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_6):
        print("CORRECT! WELL DONE!\n")
        score = score + 2
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_6, "\n\n")


time.sleep(2)

#print the score
print("==================================================")
while score >=8:
    print("SUPER AWESOME! \./\./ Your Score was", score) #paparan untuk berjaya menjawab lebih dr 4 soalan yg betul
    break

while score <8:
    print("BETTER LUCK next time! /.\/.\ Your score was", score)
    break

#Goobye message
print("Thank you for enjoying and playing the Sport Quiz Game!")