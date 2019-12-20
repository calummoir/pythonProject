import random

def randomcalc():
    score=0
    for x in range(5):
        no1=random.randint(0,9)
        no2=random.randint(0,9)
        no3=random.randint(0,9)
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
        

randomcalc()


    


