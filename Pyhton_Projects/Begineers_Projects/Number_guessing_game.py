import random




lower_bound=int(input("Enter Lower bound number for a range: "))
upper_bound=int(input("Enter Upper bound number for a range: "))

#generating a random number
Random_number=random.randint(lower_bound,upper_bound)

print("Guess my number that i have in my mind!")

while True:
    user_num=int(input("Enter your guess number: "))
    
    if (user_num==Random_number):
        print("Yeah! you have guessed a right number")
        break
    elif(user_num>Random_number):
        print("Entered guess number is greater than my guess number. Try Again: ", end="\n\n")
    else:
        print("Entered guess number is smaller than my guess number. Try Again: ", end="\n\n")



