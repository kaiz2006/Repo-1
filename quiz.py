print("Welcome to the Quiz App! Let's test your knowledge." )

import random

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = input("Please enter the number of your answer(Type exit to end the quiz): ")
    
    if options[int(answer) - 1] == correct_answer:
        print("Correct!")
        return 1  # 1 point for correct answer
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
        return 0  # 0 points for wrong answer

def start_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        }
    ]
    
    random.shuffle(questions)
    score = 0  # Initialize score

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])
    print(f"Quiz completed! Your total score is: {score}/{len(questions)}")
    print("Thank you for participating.")

if __name__ == "__main__":
    start_quiz()
    if answer == "exit:":
        print("Exiting the quiz. Goodbye!")
        exit()
    

