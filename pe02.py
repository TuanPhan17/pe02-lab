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
        while count < number:  # keep looping until we've generated the number of Fibonacci numbers the user asked for
            next_number = first + second #calculating next number 
            print(next_number)
            first = second
            second = next_number #updating two previous numbers 
            count += 1 # increase counter

elif choice == 3:
    # --- Stage of Life ---

    person_age = int(input("How old is the person? "))

    if person_age < 2:  # If the person is less than 2 years old
        print("Person is a baby.")
    elif person_age < 4:  # If the person is at least 2 but less than 4
        print("Person is a toddler.")
    elif person_age < 13:  # If the person is at least 4 but less than 13
        print("Person is a kid.")
    elif person_age < 20:  # If the person is at least 13 but less than 20
        print("Person is a teenager.")
    elif person_age < 65:  # If the person is at least 20 but less than 65
        print("Person is an adult.")
    else:  # If the person is age 65 or older
        print("Person is an elder.")


elif choice == 4:
    # --- Movie Ticket Pricing ---
    
    while True:  # USING LOOP to ask for age repeatedly 
        age_input = input("Enter the person's age (or 'q' to quit): ")
        if age_input.lower() == 'q':
            break

        person_age = int(age_input)

        if person_age < 3:  # If a person is under the age of 3
            print("Ticket is free.")
        elif person_age <= 12:  # If they are between 3 and 12
            print("Ticket is $10.")
        else:  # If they are over age 12
            print("Ticket is $15.")


elif choice == 5:
    #--- Patern printing code---

#PSEUDOCODE PATTERN PRINT 
#Ask user how many rows they want in pattern
# Example: if they say 4, we'll have 4 lines of stars 
# Start a loop that goes from 1 up to the number of rows 
#Each time loop runs , one row of stars get printed 
#inside loop , Figure out how many stars in loop, same as loop number 
#print that many stars * using repetion times loop number 
#Loop finished pattern is done 

    total_rows = int(input("Enter how many rows you want in the pattern: ")) 

    current_row = 1 # starting with first row 

    while current_row <= total_rows:  # While current row is less than or equal to total rows 

        stars = "" # We will make an empty string to keep the stars in

        count = 1
        while count <= current_row: # using inner loop to build pattern adding stars 
            stars = stars + "*"
            count = count + 1

        print(stars) # Once all stars are added, print the stars 

        current_row = current_row + 1 # Move to the next row


else:
    print("Invalid choice! Please enter 1-5.")

