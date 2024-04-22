def check_answer_correct(question, answer):
    return question.correct_answer == answer

def score_modifier(base_score):
    def calculate(answer_correct):
        if answer_correct:
            return base_score * 2
        return -50
    return calculate

class Game:
    def __init__(self, questions):
        self.questions = questions
        self._current_question_index = 0
        self._score = 0
        self.check = check_answer_correct
        self.calculate_score = score_modifier(100)

    def submit_answer(self, answer):
        current_question = self.questions[self._current_question_index - 1]
        if self.check(current_question, answer):
            self._score += self.calculate_score(True)
            return True
        else:
            self._score += self.calculate_score(False)
            return False

    def get_score(self):
        return f'{self._score} PLN'
    def __str__(self):
        return f"Current score: {self._score}"
    def __len__(self):
        return len(self.questions)
    def __getitem__(self, index):
        # return self.questions[index] if index < len(self.questions) else None
        if index < len(self.questions):
            return self.questions[index]
        else:
            None
    def __setitem__(self, index, value):
        if index < len(self.questions):
            self.questions[index] = value
        else:
            raise IndexError

    def get_next_question(self, level = None):
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            return question
        else:
            return None

    def submit_answer(self, answer):
        current_question = self.questions[self._current_question_index - 1]
        if self.check(current_question, answer):
            self._score += 100
            return True
        else:
            return False

    def get_score(self):
        return f'{self._score} PLN'


def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
    ]

    game = Game(question_list)
    print(len(game))
    print(game[0])
    game[0] = Question("What is 5 + 2?", ["3", "7", "2", "5"], "7")
    print(game[0])

if __name__ == '__main__':
    main()