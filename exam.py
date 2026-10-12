from question import Question

class Exam:
    Exam_name = "Pass and fly CBT"  

    def __init__(self):
        self.__score = 0
        self.results = []
        self.questions = [
            Question("What is the capital of Nigeria?",
                    ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"], "B"),
            Question("What is 2 + 2?",
                    ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
            Question("Which language are we using?",
                    ["A. Java", "B. C++", "C. Python", "D. PHP"], "C"),
        ]

    def take_test(self, name):
        self.__score = 0

        for question in self.questions:
            question.display_question()
            while True:
                answer = input("Enter your answer (A-D): ").strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    break
                print("Invalid answer, please enter A, B, C or D.")

            if question.check_answer(answer):
                print("Correct!")
                self.__score += 1
            else:
                print("Wrong!")
            print()

        print(f"{name}, your score is {self.__score}/{len(self.questions)}")
        self.results.append({"name": name, "score": self.__score})

    def check_result(self, name):
        for result in self.results:
            if result["name"].lower() == name.lower():
                print(f"{result['name']}, your score is {result['score']}")
                return
        print("Result not found")