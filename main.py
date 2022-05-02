import random

NOMBRE_MIN= 1
NOMBRE_MAX=10
NOMBRE_QUESTION = 4 
SCORE = 0

def poser_question():
    #a et b 
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    #get value 
    reponse = input(f"calculez : {a} + {b} =  ")
    reponse = int(reponse)
    if reponse == a + b :
        return True
        #print("reponse correct")
    # else:
    #     print("reponse incorrcet")
    return False


for i in range(0, NOMBRE_QUESTION):
    print(f"Question n°{i+1} sur {NOMBRE_QUESTION} ")
    if poser_question():
        SCORE +=1
        print("reponse correct")
    else:
        print("reponse incorrcet")
    print()

print(f" votre scrore {SCORE}/{NOMBRE_QUESTION}")
