from datetime import datetime,timezone
from django.test import TestCase
from Quiz.models import *
# Create your tests here.
class QuizModelTest(TestCase):

    def create_valid_quiz(self):
        self.quiz_title = "New Quiz"
        self.date_added = datetime.utcnow()
        self.quiz_obj = QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
        return self.quiz_obj
    
    # This should fail as the quiz_title exceeds the field limit
    def create_fail_quiz(self):
        self.quiz_title = "New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz New Quiz "
        self.date_added = datetime.utcnow()
        return QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
    
    def test_create_quiz(self):
        quiz = self.create_valid_quiz()
        # Test that a valid instance of the model is created
        self.assertTrue(isinstance(quiz, QuizModel))
        # Test that the quiz_title matches the expected value
        self.assertEqual(str(quiz), self.quiz_title)


class QuestionModelTest(TestCase):

    def create_valid_quiz(self):
        self.quiz_title = "New Quiz"
        self.date_added = datetime.utcnow()
        self.quiz_obj = QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
        return self.quiz_obj

    def create_valid_question(self):
        self.quiz = self.quiz_obj
        self.question_title = "What is a question?"
        self.question_number = 1
        self.correct_answer = "This is an answer"
        self.answer_1 = "Answer 1"
        self.answer_2 = "Answer 2"
        self. answer_3 = "This is an answer"
        self.quetion_obj = QuestionsModel.objects.create(quiz=self.quiz, question_title=self.question_title, correct_answer=self.correct_answer, answer_1=self.answer_1,answer_2=self.answer_2,answer_3=self.answer_3)
        return self.quetion_obj

    def test_create_question(self):
        # Create quiz instsance 
        self.quiz = self.create_valid_quiz()
        # Create question instance
        self.question = self.create_valid_question()
        # Check instance is valid
        self.assertTrue(isinstance(self.question, QuestionsModel))
        self.assertEqual(str(self.quiz), self.quiz_title)
        self.assertEqual(str(self.question.question_title), self.question_title)