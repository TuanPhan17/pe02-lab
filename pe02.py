# Main Menu
print("Choose a program to run:")
print("1. Prime Number Checker")
print("2. Fibonacci Sequence")
print("3. Stage of Life")
print("4. Movie Ticket")
print("5. Pattern Printing")

choice = int(input("Enter your choice (1-5): "))

#PRIME NUMBER PSEUDOCODE
#input a number
#store number
#if number is less than or equal to 1, say it's not a prime number
#then start checking all numbers starting from 2 up to half of the number
# for each number in that range, see if it divides evenely into the users number
#if any number divides evenly , users number is not prime. STOP CHECKING
#if no number divides evenly , number is prime 
# PRINT PRIME OR NOT PRIME

if choice == 1:
    # --- PRIME NUMBER PROGRAM ---
    number = int(input("Enter a number: "))  # Ask user to input number

    if number <= 1:
        print("Not Prime")  # If number less than or equal to 1, not prime
    else:
        is_prime = True  # Setting up flag variable

        for i in range(2, number // 2 + 1):  # Checking every possible divisor from 2 and up
            if number % i == 0:  # Divides evenly → NOT PRIME
                is_prime = False
                break  # Found a divisor → STOP

        if is_prime:
            print("PRIME") #PRINT RESULTS
        else:
            print("NOT PRIME")


# Fibonacci pseudocode
# how many fibonacci numbers to generate
#store number
#start w/ two numbers 0 & 1 - first two in sequence
#if user wants 1 number , print 0
#otherwise, print 0 & 1 as starting numbers
# Use loop to keep adding last two numbers together to make next one.
#each time calculating new number , print it 
#Keep doing that until printed as many numbers as user asked 

elif choice == 2:
    # --- Fibonacci Number Program ---
    number = int(input("How many Fibonacci numbers do you want to generate? ")) # input number

    if number <= 0: #if input invalid
        print("Enter positve number")

    elif number == 1: #if user wants 1 number
        print("0")

    else:
        first = 0
        second = 1  #Start w/ first two numbers in sequence 
        
        print(first)
        print(second)

        # USING LOOP TO GENERATE REST 
        count = 2 # already printed 2 numbers 

        while count < number: 
            next_number = first + second #calculating next number 

            print(next_number)

            first = second
            second = next_number #updating two previous numbers 

            count += 1 # increase counter


