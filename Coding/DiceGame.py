from random import randint
guess=randint(1,20)


guess_no = int(input("Enter the Number"))

if guess_no==guess:
    print("Congratulations")
else:
    print("Your answer is Incorect")
    print("Number was",guess)