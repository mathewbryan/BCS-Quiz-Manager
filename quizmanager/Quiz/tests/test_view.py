from datetime import datetime,timezone
from django.http import request
from django.test import TestCase
from django.contrib.auth.models import User
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

class TestQuestionsView(TestCase):

    def create_valid_quiz(self):
        self.quiz_title = "New Quiz"
        self.date_added = datetime.utcnow()
        self.quiz_obj = QuizModel.objects.create(quiz_title=self.quiz_title, date_added=self.date_added)
        return self.quiz_obj

    # Test List View
    def test_list_view(self):
        self.quiz = self.create_valid_quiz()
        self.quiz_id = 1
        view = Questions()
        view.setup(self.quiz)
        self.request = request.HttpRequest()
        self.request.user = User.objects.create_user('test', password='test')
        self.request.user.is_superuser=True
        self.request.user.is_staff=True
        self.request.user.is_active = True
        self.request.user.save()
        
        
        context = view.get_context_data()
        context_quiz_title = str(context['quizzes'][0])
        self.assertEqual(context_quiz_title, self.quiz_title)
