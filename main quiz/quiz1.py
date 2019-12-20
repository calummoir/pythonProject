import time #This allows use of time in seconds
import sys
import random
score =0 #sets the score to 0
sec =0 #sets the time to 0

def login(): 
    sec =0
    print("Welcome!")
    for x in range(5): #this repeats this section of code 5 times
        password = input("Enter the password: ")
        if password=="1234":
            account() #if they get it correct it then it moves to account
        elif password=="xd":
            print("Hello Master Calum")
            choice()
        else:
            sec=sec+2 #everytime they get it wrong it adds 2 more seconds
            print("Try Again!")
            time.sleep(sec) #this stops the code for the amount of time
    print("You can't play my quiz :(") #if they get it wrong 5 times it stops
            

def account():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    print("Hello",name)
    time.sleep(1)
    choice() #moves to choice

def choice():
    print("What quiz do you want to play?")
    quiztype=int(input("1, 2, 3 or 4? ")) #asks for which quiz
    if quiztype== 1:
        print ("You have chosen quiz 1")
        quiz1() #goes to quiz 1
    elif quiztype== 2:
        print ("You have chosen quiz 2")
        quiz2() #goes to quiz 2
    elif quiztype== 3:
        print ("You have chosen quiz 3")
        quiz3() #goes to quiz 3
    elif quiztype== 4:
        print("You have chosen quiz 4")
        quiz4()
    else:
        print("Choose 1, 2, 3 or 4")
        time.sleep(1)
        choice() #if they dont choose a quiz it repeats
       
                 
def quiz1():
    score =0
    print("Quiz 1")
    print("Q1: What is 9+1? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 19:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q2: What is 2+2? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 4:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q3: What is 4-1? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 3:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q4: What is 6+6+6? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 18:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q5: What is 9+0? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 9:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")
    print("You got",score,"question right out of 5")
    time.sleep(1)
    replay()

def quiz2():
    score =0
    print("Quiz 2")
    print("Q1: What is 2+2-1? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 3:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q2: What is -4*4+15? ")
    ans1=int(input("Enter answer here: "))
    if ans1== -1:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q3: What is 4-1*3? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 1:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q4: What is 6*6-6? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 30:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")

    print("Q5: What is 6-6/6? ")
    ans1=int(input("Enter answer here: "))
    if ans1== 5:
        print("Correct!")
        score= score+1
    else:
        print("Wrong!")
    print("You got",score,"question right out of 5")
    time.sleep(1)
    replay()

def quiz3():
    score =0
    print("Quiz 3")
    print("Q1: What is the capitial of Brazil? ")
    ans1=input("Enter answer here: ").lower()
    if ans1== "brasilia":
        print("Correct!")
        score= score+1
    else:
        print("Wrong it's Brasilia!")

    print("Q2: What is the capitial of England? ")
    ans1=input("Enter answer here: ").lower()
    if ans1== "london":
        print("Correct!")
        score= score+1
    else:
        print("Wrong it's London!")

    print("Q3: What is the capitial of Germany? ")
    ans1=input("Enter answer here: ").lower()
    if ans1== "berlin":
        print("Correct!")
        score= score+1
    else:
        print("Wrong it's Berlin!")

    print("Q4: What is the capitial of Russia? ")
    ans1=input("Enter answer here: ").lower()
    if ans1== "moscow":
        print("Correct!")
        score= score+1
    else:
        print("Wrong it's Moscow!")

    print("Q5: What is the capitial of Australia? ")
    ans1=input("Enter answer here: ").lower()
    if ans1== "canberra":
        print("Correct!")
        score= score+1
    else:
        print("Wrong it's Canberra!")
    print("You got",score,"question right out of 5")
    time.sleep(1)
    replay()

def quiz4():
    score=0
    for x in range(5):
        no1=random.randint(1,9)
        no2=random.randint(1,9)
        no3=random.randint(1,9)
        ops=("/", "*", "-", "+")
        op1=(random.choice(ops))
        op2=(random.choice(ops))
        ans=eval(("{0} {1} {2} {3} {4}").format(no1, op1, no2, op2, no3))
        question="What is {0}{1}{2}{3}{4} = ".format(no1, op1, no2, op2, no3)
        q1=float(input(question))
        if q1==(ans):
            score=score+1
            print("Correct!")
        else:
            print("Wrong it is",ans)
    print("You got",score,"question right out of 5")
    time.sleep(1)
    replay()
   

def replay():
    time.sleep(1)
    retry=input("Would you like to play another quiz?(yes or no) ").lower()
    if retry=="yes":
        choice()
    else:
        end()


def end():
    print("Thank you for playing")
    sys.exit()


login()


























