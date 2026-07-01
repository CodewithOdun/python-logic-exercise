#Import time to add effects
import time
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
#Repeation block,
while True:    
    # Removed the redundant str() since input() is already a string
    student_name = input("Enter your name: ")
    student_age = int(input("Enter your age: "))  
    print("Loading...")
    time.sleep(2)
    print(f"Your name is {YELLOW}{student_name}{RESET}, and you are {YELLOW}{student_age}{RESET} years old.")
    time.sleep(1)

    
    # Fixed the typo from 'compartibility' to 'compatibility'
    print("\nAge compatibility verification...")
    time.sleep(2)
    print("Checking status... Please wait.")
    time.sleep(2)
    
    # Clear logic
    if student_age >= 16:
        print(f"Result: {GREEN}You are eligible for the poll.{RESET}")
    else:
        print(f"Result: {RED}You are not eligible for the poll.{RESET}")
