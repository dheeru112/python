#the perfect guess
import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    guesses+=1 
    a = int(input("Guess a number:"))
    if(a>n):
        print("lower number please")
    else:
        print("higher number please") 

print(f"you guessed the number in {guesses} attempts")  

