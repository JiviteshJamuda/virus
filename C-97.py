import random

print("Oh No! Your system has been attacked by a virus \nRules : \n - To free your system you have to guess the hidden number between 1 to 9 \n - We will help you by telling whether your number is lesser or greater than the hidden number \n - You will get 5 chances for guessing the correct number \n - If you guess the correct number then your system will get free from this virus \n - If you lose all of your chances then your system is going to GET REKT!")
rng = random.randint(1,9)
noOfChances = 0

while noOfChances < 5 :
    num = int(input("Enter a number : "))
    if num == rng :
        print("you won")
        break
    elif num < rng :
        print("your guess was low guess a higher number\n")
    else :
        print("your guess was higher guess a lower number\n")
    noOfChances = noOfChances + 1

if not noOfChances < 5 :
    print("!@#$%^&*( The Number Was : ", rng, ")*&^%$#@!")
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!! \n!!! Deploying Viruses !!! \n!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    print("          II\n         I  I\n        I    I\n       I      I\n      I        I\n     I          I\n    I            I\n   I              I\n  I                I\n I------------------I")
    