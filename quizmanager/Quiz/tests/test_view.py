from datetime import datetime,timezone
from django.test import TestCase
from Quiz.views import *

class TestListView(TestCase):

    def create_valid_quiz(self):
        self.quiz_title = "New Quiz"
        self.date_added = datetime.utcnow()
        self.quiz_obj = QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
        return self.quiz_obj

    # Test List View
    def test_list_view(self):
        self.quiz = self.create_valid_quiz()
        view = List()
        view.setup(self.quiz)
        context = view.get_context_data()
        context_quiz_title = str(context['quizzes'][0])
        self.assertEqual(context_quiz_title, self.quiz_title)