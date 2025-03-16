# An Interactive Mathematics Quiz Game

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

