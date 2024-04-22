import json
from question import Question


def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    questions = []
    for item in data:
        question = Question(
            item['question'],
            item['options'],
            item['correct_answer'],
            item['difficulty']
        )
        questions.append(question)
    return questions
