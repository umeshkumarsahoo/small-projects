theme="#375362"
from quiz_brain import QuizBrain
from tkinter import *
from typing import Any
class Interface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quizzzer")
        self.window.config(padx=20,pady=20,bg=theme)

        self.score=0
        self.score_label=Label(text=f"Score:{self.score}",fg="white",bg=theme)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=400,height=200,bg="white")
        self.question_text=self.canvas.create_text(150,100,width=300,text="some question",fill=theme,font=("Roboto",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.true=Button(text="✔️",highlightthickness=0,padx=0,pady=0,command=self.right)
        self.true.grid(row=2,column=0)
        self.false=Button(text="❌",highlightthickness=0,padx=0,pady=0,command=self.wrong)
        self.false.grid(row=2,column=1)
        self.get_next()
        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
    def right(self):
        ans=self.quiz.check_ans("true")
        self.give_feedback(ans)
    def wrong(self):
        ans=self.quiz.check_ans("false")
        self.give_feedback(ans)
    def give_feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
            self.score+=1
            self.score_label.config(text=f"Score:{self.score}")
        else:
            self.score+=0
            self.score_label.config(text=f"Score:{self.score}")
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)
