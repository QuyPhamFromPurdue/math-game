import random
import time
import threading


"""
MathGameByQuy - An Interactive Mathematics Quiz Game

This game is designed to test and improve mathematical skills through timed arithmetic challenges.
Players can choose different difficulty levels and set their own time limits for solving problems.

Authors: Quy Pham

Key Features:
    - Multiple difficulty levels (Easy, Medium, Hard)
    - Customizable time limits per question
    - Real-time countdown timer
    - Score tracking
    - Input validation and error handling

Classes and Functions:

    generate_question(difficulty: str) -> tuple
        Generates a random math question based on the chosen difficulty level.
        Args:
            difficulty: String ('A', 'B', or 'C') representing the difficulty level
        Returns:
            tuple: (question string, correct answer)

    check_answer(question: str, answer: float, time_limit: int) -> bool
        Handles user input and validates the answer within the time limit.
        Args:
            question: String containing the math problem
            answer: Float containing the correct answer
            time_limit: Integer representing seconds allowed for answering
        Returns:
            bool: True if answer is correct and within time limit, False otherwise

    countdown_timer(time_limit: int, stop_event: threading.Event) -> None
        Displays a real-time countdown timer.
        Args:
            time_limit: Integer representing seconds to count down from
            stop_event: Threading event to control timer termination

    play_game() -> None
        Main game loop that manages the gameplay flow and user interaction.

Usage:
    Run the script and follow the prompts to:
    1. Choose to start the game (Y/N)
    2. Select difficulty level (A/B/C)
    3. Set time limit per question
    4. Solve math problems within the time limit
    5. Type 'stop' to end the game and see final score
"""


def countdown_timer(time_limit, stop_event):
    for remaining in range(time_limit, 0, -1):
        if stop_event.is_set():
            return
        print(f"\033[F\033[KTime remaining: {remaining} seconds")
        time.sleep(1)


# Function to generate a random math question based on the chosen difficulty
def generate_question(difficulty):
    while 1:
        if difficulty in ["A", "a"]:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(["+", "-"])
            break
        elif difficulty in ["B", "b"]:
            num1 = random.randint(2, 20)
            num2 = random.randint(2, 20)
            operator = random.choice(["*", "/"])
            if num1 % num2 > 0 or num1 == num2: 
            # Ensure that when a/b, the answer is a whole number and not decimal
            # Ensure a != b so the equation is more challanging (because if a = b => a/b = 1)
                continue
            else:
                break
        elif difficulty in ["C", "c"]:
            num1 = random.randint(5, 50)
            num2 = random.randint(5, 20)
            operator = random.choice(["+", "-", "*", "/"])
            if num1 % num2 > 0 or num1 == num2:
            # Ensure that when a/b, the answer is a whole number and not decimal
            # Ensure a != b so the equation is more challanging
                continue
            else:
                break
        else:
            print("Invalid difficulty choice.")
            return None
    
    question = str(num1) + " " + operator + " " + str(num2)
    answer = eval(question)
    return question, answer

# Function to check if the answer is correct
def check_answer(question, answer, time_limit):
    stop_event = threading.Event()
    timer_thread = None
    try:
        print(f"\nWhat is {question}?")
        print("")  # Add empty line for timer
        
        timer_thread = threading.Thread(target=countdown_timer, args=(time_limit, stop_event))
        timer_thread.daemon = True
        timer_thread.start()
        
        start_time = time.time()
        user_answer = float(input())
        elapsed_time = time.time() - start_time
    except:
        stop_event.set()
        if timer_thread:
            timer_thread.join()  # Wait for timer to fully stop
        print("\nInvalid input. Please enter a number.")
        return False
    finally:
        # Always stop the timer and wait for it to finish
        stop_event.set()
        if timer_thread:
            timer_thread.join()
        print("\n")  # Add a new line to separate from timer
    
    if elapsed_time > time_limit:
        print("Time's up! You missed this one.")
        return False
    
    if user_answer == answer:
        return True
    else:
        return False

# Main game function
def play_game():
    print("== MATH QUIZ! ==")
    print("Give correct answers to get scores for a given time limit")
    score = 0
    while True:
        difficulty = input("Level difficulties: \n A. Easy (+ and -) \n B. Medium (* and /) \n C. Hard (+, -, *, /) \n Choose your level: ")
        if difficulty in ["A", "B", "C", "a", "b", "c"]:
            break
        else:
            print("Invalid input. Please choose A, B, or C.")
    
    time_limit = int(input("Enter time limit for each question (in seconds): "))
    
    while True:
        question, answer = generate_question(difficulty)
        print("\nYou have {} seconds to answer the following question:".format(time_limit))
        
        # Store the result of check_answer
        result = check_answer(question, answer, time_limit)
        
        if result == True:  # Check if the answer is correct
            score += 1
            print("Correct! Score: ", score)
        elif result == False:  # Check if the answer is incorrect
            print("Incorrect! The correct answer is: ", answer) 
            print("Score: ", score)

        continue_or_stop = input("Type 'stop' to see your total score or press Enter to continue: ")
        if continue_or_stop == "stop":
            print("--- Thank you for playing ---")
            print("Your total score is:", score)
            break



# Run the game
print("== WELCOME TO QUICK-THINKING MATH GAME ==")
print("By: Quy Pham Ngo Thien")
while 1:
    join_the_game = input("Start the game? (Y: Yes/ N: No): ")
    if join_the_game in ["Y", "N", "y", "n"]:
        if join_the_game in ["Y", "y"]:
            play_game()
        elif join_the_game in ["N", "n"]:
            print("--- Thank you for playing ---")
            break
    else:
        print("Invalid Input")
