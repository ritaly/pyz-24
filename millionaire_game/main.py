from game import Game
from hinted_game import HintGame
from fileloader import load_questions_from_file
from timed_game import TimedGame

def play_game(game):
    print("Welcome to the Millionaire Game!\n")
    while True:
        question = game.get_next_question()
        print(question)

        if isinstance(game, HintGame):
            while True:
                resp = input('Do you need a hint? Y/N').upper()
                if resp == 'Y':
                    game.request_hint(question)
                    break
                elif resp == 'N':
                    break
                else:
                    print('No such option; Try again!')

        if not question:
            print("Congratulations! You've completed the game.")
            break

        answer = input("Please enter the number of your answer: ")

        if game.submit_answer(question.options[int(answer) - 1]):
            print("The correct answer --> ", question.correct_answer)
            print(f"Current score: {game.get_score()}")
        else:
            break
    print(f"Your final score is: {game.get_score()}")

def difficulty_filtr(level):
    def filter_questions(question):
        return question.difficulty == level
    return filter_questions

def main():
    question_list = load_questions_from_file('questions.json')
    # TO-DO: dodać odczytywanie poziomu od użytkownika
    easy_questions = list(filter(difficulty_filtr('easy'), question_list))


    while True:
        quests = """What kind of game you wanna play
         1 - normal
         2 - with hints
         3 - timed
          Select -> """

        selected_game = input(quests)
        if selected_game == '1':
            game_instance = Game(question_list)
            break
        elif selected_game == '2':
            game_instance = HintGame(question_list, 3)
            break
        elif selected_game == '3':
            game_instance = TimedGame(question_list, 20)
            break
        else:
            print('No such option, please try again')

    play_game(game_instance)

if __name__ == "__main__":
    main()