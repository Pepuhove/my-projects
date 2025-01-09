print("WELCOME TO THE QUIZ GAME! ")

playing = input("Do you wanna play? ")
score=0
amount=0
if playing == "yes"or "YES" or "Yes" :
    print("Okay! lets play :")
else:
    quit()
   
answer = input("What does cpu stands for? ").upper()
if answer == ("CENTRAL PROCESSING UNIT"):
    print("correct")
    score+=1
    amount+=5
else:
    print("Incorrect")
    quit()
playing=input("Do you wanna play again? ")
if playing !="yes"or "YES" or "Yes" :
    print("lets go on!")
else:
    quit()
answer=input("what is the capital city of Zimbabwe? ").upper()
if answer.upper()==("HARARE"):
    print("good")
    score+=1
    amount+=5
else:
    print("Oh NO!")
print("You got "+ str(score)  + " questions answered correctly!\nYou got " + str((score//2)*100)+"%" f" and your actually prize is ${amount}.")
    
