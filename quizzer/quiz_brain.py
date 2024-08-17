import html

class QuizBrain:
    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0

    def still_has_qus(self):
        if self.question_no<len(self.question_list):
            return True

    def next_question(self):
        self.curr_question=self.question_list[self.question_no]
        self.question_no+=1
        q_text=html.unescape(self.curr_question.text)
        return f"Q.{self.question_no}:{q_text}(True/False): "

    def check_ans(self,answer):
        if answer.lower()==self.curr_question.answer.lower():
            self.score+=1
            return True
        else:
            return False
        # print(f"correct answer to the qus is {correct}")
        # print(f"your current score is: {self.score}/{self.question_no}")
