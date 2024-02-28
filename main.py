from untils import *
from question import *


def main():
    score = 0
    right_answers = 0
    print('Игра начинается!')

    for i in range(5):
        qwerty = random_question()
        question = Question(qwerty['q'], qwerty['d'], qwerty['a'])

        print(question.build_question())
        question.user_answer = input()
        if question.is_correct(question.user_answer):
            right_answers += 1
            score += question.points
        print(question.build_feedback())
    print(f'Вот и всё!\nОтвечено {right_answers} вопроса из 5\nНабрано баллов: {score}')


main()
