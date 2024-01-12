import random

class QuizGame:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.user_score = 0

    def add_question(self, question, options, correct_option):
        self.questions.append({"question": question, "options": options, "correct_option": correct_option})

    def display_question(self, question_obj):
        print(question_obj["question"])
        for idx, option in enumerate(question_obj["options"], 1):
            print(f"{idx}. {option}")
        user_answer = input("Enter the number of your answer: ")
        return int(user_answer)

    def evaluate_answer(self, user_answer, correct_option):
        if user_answer == correct_option:
            print("Correct!\n")
            self.user_score += 1
        else:
            print(f"Wrong! The correct answer is {correct_option}. \n")

    def run_quiz(self):
        print("Welcome to the Quiz Game!\n")
        for idx, question_obj in enumerate(self.questions, 1):
            print(f"Question {idx}:")
            user_answer = self.display_question(question_obj)
            correct_option = question_obj["correct_option"]
            self.evaluate_answer(user_answer, correct_option)

        print(f"Quiz completed! Your final score is {self.user_score}/{len(self.questions)}.")

if __name__ == "__main__":
    quiz = QuizGame()

    # Add your questions here
    quiz.add_question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
    quiz.add_question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)
    quiz.add_question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 2)

    quiz.run_quiz()
