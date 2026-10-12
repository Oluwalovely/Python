class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_question(self):
        print(self.question)

        for option in self.options:
            print(option)

    def check_answer(self, user_answer):
        if user_answer.upper() == self.answer.upper():
            return True
        else:
            return False