class Question:

    def __init__(self, text, hard, answer):
        self.text = text
        self.hard = hard
        self.answer = answer

        self.user_answer = None
        self.points = int(self.hard) * 10

    def get_points(self):
        return self.points

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def build_question(self):
        return f'Вопрос: {self.text}\nСложность: {self.hard}/5'

    def build_feedback(self):
        if self.is_correct(self.user_answer):
            return f'Ответ верный, получено {self.points} баллов'
        return f'Ответ неверный, верный ответ {self.answer}'
