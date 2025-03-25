import random

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Your choice (1-4): "))
            if 1 <= answer <= 4:
                return options[answer - 1] == correct_answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 4.")

def quiz_game():
    questions = {
        "Python": [
            ("What is the output of print(2 ** 3)?", ["5", "6", "8", "9"], "8"),
            ("Which keyword is used to define a function in Python?", ["func", "define", "def", "lambda"], "def"),
            ("What is the correct file extension for Python files?", [".py", ".pt", ".pyt", ".python"], ".py"),
        ],
        "Movies": [
            ("Who directed the movie 'Inception'?", ["Steven Spielberg", "Quentin Tarantino", "Christopher Nolan", "James Cameron"], "Christopher Nolan"),
            ("Which movie features the quote 'I'll be back'?", ["Terminator", "Rocky", "Die Hard", "RoboCop"], "Terminator"),
            ("What is the name of the main protagonist in 'The Matrix'?", ["Neo", "Morpheus", "Trinity", "Agent Smith"], "Neo"),
        ]
    }
    
    print("Welcome to the Quiz Game! 🎮")
    while True:
        print("\nChoose a topic:")
        for i, topic in enumerate(questions.keys(), 1):
            print(f"{i}. {topic}")
        
        try:
            choice = int(input("Enter the number of your chosen topic: "))
            if choice in [1, 2]:
                topic = list(questions.keys())[choice - 1]
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input! Enter a number.")
    
    score = 0
    random.shuffle(questions[topic])
    
    for q in questions[topic]:
        if ask_question(q[0], q[1], q[2]):
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was: {q[2]}")
    
    print(f"\nGame Over! Your final score: {score}/{len(questions[topic])}")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()
    else:
        print("Thanks for playing! 🎉")

if __name__ == "__main__":
    quiz_game()
