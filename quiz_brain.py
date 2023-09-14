class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        varRandom = self.question_list[self.question_number].text
        varAnswer = self.question_list[self.question_number].answer
        self.question_number +=1
        user_answer = input(f"Q{self.question_number}: {varRandom} (True/False)?:")
        self.check_answer(user_answer, varAnswer)

    def still_has_questions(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("your answer is correct")
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("your answer is wrong")
            print(f"Your score is {self.score}/{self.question_number}")



