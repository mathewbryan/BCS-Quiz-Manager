from django.shortcuts import render
from django.views.generic.base import TemplateView
from Quiz.models import *
# Create your views here.
class Index(TemplateView):
    template_name = "Quiz/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.all()
        context['questions'] = QuestionsModel.objects.all()
        return context