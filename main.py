import requests
from question_sample import Question
from quiz_meter import QuizMeter
from gui import AppInterface


# We need to create yes & no questions with help of the request module
parameters = {"amount": 20, "type": "boolean"}
response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
# This is raw data of questions
questions = data["results"]

# We are creating Question Class objects which will have text and answer attributes
question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # then store them in question bank list


# Now we are going to use this question list create an instance for Quiz

# QuizMeter is going to check question counts and answers
quiz = QuizMeter(question_bank)

# Interface is responsible for how our app & it's questions looks, and gives feedback to user about their choice.
quiz_interface = AppInterface(quiz)
