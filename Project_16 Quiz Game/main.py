from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create question objects and add them to the question_bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Start the quiz
while quiz.still_has_questions():
    quiz.next_question()

# Print final score after all questions have been answered
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
