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


