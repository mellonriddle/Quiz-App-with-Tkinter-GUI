from tkinter import *
from quiz_meter import QuizMeter
THEME_COLOR = "#375362"


# Interface takes current question from QuizMeter and displays it with helps of tkinter,
# then give feedback to user when they choose an answer
class AppInterface:
    def __init__(self, quiz_meter: QuizMeter):    # This is a reminder that interface needs a QuizMeter class object
        self.quiz = quiz_meter
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        self.quest_text = self.canvas.create_text(150, 125, width=280, text="Mellon", font=("Ariel", 15, "italic"))
        ok_image = PhotoImage(file="images/true.png")
        self.ok_button = Button(image=ok_image, highlightthickness=0, command=self.user_go_ok)
        self.ok_button.grid(row=2, column=0)
        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.user_go_x)
        self.x_button.grid(row=2, column=1)
        self.score_label = Label(text=f"Score: 0", font=("Ariel", 10), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quest_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quest_text, text="You have reached end of the quiz.")
            self.x_button.config(state="disabled")
            self.ok_button.config(state="disabled")

    def user_go_x(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def user_go_ok(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
