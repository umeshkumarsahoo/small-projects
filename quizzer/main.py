from question_model import Question
from data import question_data
from ui import Interface
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))
quiz=QuizBrain(question_bank)
quiz_ui=Interface(quiz)
