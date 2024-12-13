from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os
question_list=[]
for question in question_data:
    q_quest=question["text"]
    q_answer=question["answer"]
    question_list.append(Question(q_quest,q_answer))
quiz=QuizBrain(question_list)

while quiz.current_question_index<len(question_list):
    # os.system('cls')
    quiz.ask_question()
    # print(f"score:{quiz.score}/{len(question_list)}")

print("you have completed the quiz")
print(f'your final score is :{quiz.score}/{len(question_list)}')
