from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

empty_list = []
for data in question_data:
    question_model_object = QuestionModel(data["text"], data["answer"])
    empty_list.append(question_model_object)
#print(empty_list)

quiz_brain_object = QuizBrain(empty_list)
quiz_brain_object.next_question()

while quiz_brain_object.still_has_questions() == True:
    quiz_brain_object.next_question()
