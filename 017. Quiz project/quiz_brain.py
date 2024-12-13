class QuizBrain:
    def __init__(self,questions):
        self.current_question_index=0
        self.questions=questions
        self.score=0

    def ask_question(self):
        current_question=self.questions[self.current_question_index]
        self.current_question_index +=1
        user_answer=input(f"Q{self.current_question_index}: {current_question.text} (True/False)\n score {self.score}/{len(self.questions)}: \n")

        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("correct")
            self.score+=1
        else:
            print("Thats wrong")
