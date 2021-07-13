from datetime import datetime,timezone
from django.test import TestCase
from Quiz.models import *
from Quiz.forms import *

class TestQuizForm(TestCase):

    def set_up(self):
        self.quiz_title = "New Quiz"
        self.date_added = datetime.utcnow()
        self.quiz_obj = QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
        return self.quiz_obj

    # Test valid form data
    def test_form_valid(self):
        form_data = {"quiz_title": "New Quiz", "date_added":datetime.utcnow()}
        form = CreateQuizForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Test invalid form data
    def test_form_invalid(self):
        form_data = {"quiz_title_incorrect": datetime.utcnow(), "date_added":123.111}
        form = CreateQuizForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestQuestionForm(TestCase):

    def test_form_invalid(self):
        form_data = {
            "question_title":"Question number 1",
            "question_number": "Not a number",
            "answer_1":"",
            "answer_2": "",
            "answer_3": "Answer 3",
            }
        form = CreateQuestionForm(data=form_data)
        self.assertFalse(form.is_valid())